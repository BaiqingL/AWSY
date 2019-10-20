import locateAddress, reverseAddressLookup, wigleLocation

testID = "305a3aa0da30"

googleAPI = locateAddress.GooglePlaces()

#try:
#    (loc_x, loc_y) = wigleLocation.getCoordinates(testID)
#except:
#    (loc_x, loc_y) = temp.get_coordinates(testID)

loc_x, loc_y = 37.54036713, -121.94658661
zillowAPI = locateAddress.ZillowAPI(loc_x, loc_y)

if(zillowAPI.isHouse()):
    data = reverseAddressLookup.sendRequest(googleAPI.get_address(loc_x, loc_y))

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
