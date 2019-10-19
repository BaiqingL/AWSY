import requests
import json
import time
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
from geopy.geocoders import GoogleV3
import pandas as pd
import re


zillowKey = 'X1-ZWz17kv04h00sr_2m43a'
googleKey = "AIzaSyCdbYjagJu727nxM-h5zsyuOEfhy2BxnMo"

class GooglePlaces(object):
    def __init__(self, loc_x, loc_y):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.location = loc_x+","+loc_y

    def get_address(self):
        geolocator = GoogleV3(api_key=googleKey)
        locations = geolocator.reverse(loc_x + ", " + loc_y)
        address = locations[0].address.split(",")
        print(address)
        return address


    def search_places_by_coordinate(self, radius=100):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': self.location,
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

    def get_points_of_interest(self):
        places = self.search_places_by_coordinate()
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
        locations = geolocator.reverse(loc_x + ", " + loc_y)

        f = locations[0].address.split(",")
        n = re.sub("[^0-9]", "", f[2])

        self.address = f[0] +"," + f[1]
        self.zipcode = n
        self.zillow_data = ZillowWrapper(zillowKey)

    def isHouse(self):
        try:
            deep_search_response = zillow_data.get_deep_search_results(address,n)
            return True
        except:
            return False

    def getResults(self):
        deep_search_response = self.zillow_data.get_deep_search_results(self.address, self.zipcode)
        result = GetDeepSearchResults(deep_search_response)
        return result
