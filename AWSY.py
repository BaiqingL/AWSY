import Locator
import ReverseAddressLookup
import WigleLocation
import sys

# Link together APIs and print results
def run(bssid_raw):
    bssid = bssid_raw

    googleAPI = Locator.GooglePlaces()

    try:
        (loc_x, loc_y) = WigleLocation.getCoordinates(bssid)
    except:
        (loc_x, loc_y) = googleAPI.get_coordinates(bssid)


    zillowAPI = Locator.ZillowAPI(loc_x, loc_y)

    if(zillowAPI.isHouse()):
        address = googleAPI.get_address(loc_x, loc_y)
        data = ReverseAddressLookup.sendRequest(address)

        for resident in data["current_residents"]:
            for key, val in resident.items():
                try:
                    print(key + ": " + val)
                except:
                    print(key + ": ")
                    if(key == "associated_people"):
                        print([person["relation"] + ": " + person["name"] for person in val])
                    if(key == "historical_addresses"):
                        print(["%s, %s %s %s, %s" %(address["street_line_1"], address["city"], address["state_code"], address["postal_code"], address["country_code"]) for address in val])
            print()
    df = googleAPI.get_points_of_interest(loc_x,loc_y)
    print(df.head())

if(len(sys.argv) > 2):
    print("Usage: python AWSY.py <bssid>")
else:
    run(sys.argv[1])


