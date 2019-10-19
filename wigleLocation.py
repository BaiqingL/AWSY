from pygle import network

def getCoordinates(bssid):
    formatted = "".join([bssid[i:i+2] + ":" for i in range(0, len(bssid), 2)])[:-1]

    print("Searching WiGLE.net:", formatted)

    data = network.search(netid=formatted)

    try:
        return data['results'][0]['trilat'], data['results'][0]['trilong']
    except:
        print("Invalid BSSID or BSSID not found on WiGLE.net")

print(getCoordinates("00FEC82D7B02"))



