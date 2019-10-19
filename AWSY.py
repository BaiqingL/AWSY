import locateAddress, reverseAddressLookup, wigleLocation

testID = "00FEC82D7B02"

(loc_x, loc_y) = wigleLocation.getCoordinates(testID)

temp = locateAddress.GooglePlaces(loc_x, loc_y)

data = reverseAddressLookup.sendRequest(temp.get_address())

print(data["current_residents"])
