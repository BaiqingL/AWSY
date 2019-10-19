from pygle import network

# You will have to set up your user and password for WiGLE in the pygle configuration file
def getCoordinates(bssid):
    formatted = "".join([bssid[i:i+2] + ":" for i in range(0, len(bssid), 2)])[:-1]

    print("Searching WiGLE.net:", formatted)

    data = network.search(netid=formatted)

    print(data)

    try:
        return data['results'][0]['trilat'], data['results'][0]['trilong']
    except:
        print("Invalid BSSID, BSSID not found on WiGLE.net, or too many queries today")




