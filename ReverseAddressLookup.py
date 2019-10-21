import requests
import json

ekataKey = "5cec97f82b294b0cb0de3c11ddc9a76a"

def sendRequest(address):
    """
    Queries the given address to the Ekata api and returns
    the json data as a dict().

    Note that 'address' is a list given in the following format:
    ["NUM STREET", "CITY", "STATE ZIP", "COUNTRY"]

    """

    street = address[0]
    city = address[1]
    state, zipcode = address[2].split()
    country = address[3]


    parameters = {
        "api_key": ekataKey,
        "city": city,
        "country_code": country,
        "postal_code": zipcode,
        "state_code": state,
        "street_line_1": street
    }

    url = "https://api.ekata.com/3.0/location"

    response = requests.get(url, params=parameters)
    data = response.json()

    return data

