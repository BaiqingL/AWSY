import requests
import json
import time
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
from geopy.geocoders import GoogleV3
import pandas as pd
import re

# Put your api keys here
zillowKey = "api_key"
googleKey = "api_key"

class GooglePlaces(object):
    def __init__(self):
        self.loc_x = None
        self.loc_y = None
        self.location = None

    def get_address(self, loc_x, loc_y):
        geolocator = GoogleV3(api_key=googleKey)
        location = str(loc_x)+","+str(loc_y)
        locations = geolocator.reverse(location)
        address = locations[0].address.split(",")
        print("Address: ")
        print(address)
        print()
        return address

    def get_coordinates(self, bssid):
        endpoint_url = "https://www.googleapis.com/geolocation/v1/geolocate" + "?key=" + googleKey
        formatted = "".join([bssid[i:i+2] + ":" for i in range(0, len(bssid), 2)])[:-1]
        print(formatted)
        headers = {"Content-Type": "application/json"}
        params = {
            "considerIp": "false",
            "wifiAccessPoints": [
                {
                    "macAddress":  formatted[:-1] + "d"
                },
                {
                    "macAddress": formatted
                }
            ]
        }
        results = requests.post(endpoint_url, data = json.dumps(params), headers = headers)
        results = json.loads(results.content)
        print(results)
        return results["location"]["lat"], results["location"]["lng"]


    def search_places_by_coordinate(self,loc_x,loc_y, radius=100):
        location = str(loc_x)+","+str(loc_y)
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'key': googleKey
        }
        results = requests.get(endpoint_url, params = params)
        results =  json.loads(results.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(5)
        return places

    def get_points_of_interest(self,loc_x,loc_y):
        places = self.search_places_by_coordinate(loc_x,loc_y)
        d = {'types': []}
        df = pd.DataFrame(data=d)
        setter =3
        if(len(places)<3):
            setter = len(places)

        for z in range(0,setter):
            x = places[z]
            if "price_level" in x:
                f = {'name': [x["name"]],'types': [x["types"]],'price_level': [x["price_level"]]}
            else:
                f = {'name': [x["name"]],'types': [x["types"]],'price_level': ["null"]}
            lf = pd.DataFrame(data=f)
            df = df.append(lf, ignore_index=True)
        return df

class ZillowAPI(object):
    def __init__(self, loc_x, loc_y):
        geolocator = GoogleV3(api_key=googleKey)
        locations = geolocator.reverse(str(loc_x) + ", " + str(loc_y))

        f = locations[0].address.split(",")
        n = re.sub("[^0-9]", "", f[2])

        self.address = f[0] +"," + f[1]
        self.zipcode = n
        self.zillow_data = ZillowWrapper(zillowKey)

    def isHouse(self):

        deep_search_response = self.zillow_data.get_deep_search_results(self.address, self.zipcode)
        try:
            return True
        except:
            return False

    def getResults(self):
        deep_search_response = self.zillow_data.get_deep_search_results(self.address, self.zipcode)
        result = GetDeepSearchResults(deep_search_response)
        return result
