import requests
import json

API_KEY = "your_ekata_api_key"

# Address format (list):  ["NUM STREET", "CITY", "STATE ZIP", "COUNTRY"]
def sendRequest(address):
    street = address[0]
    city = address[1]
    state, zipcode = address[2].split()
    country = address[3]


    parameters = {
        "api_key": API_KEY,
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

