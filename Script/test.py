import requests
import json

COUNTRIES_URL = "https://restcountries.com/v3.1/"
country_request = input("Which country would you like to choose?: ")

rawdata = requests.get(COUNTRIES_URL + "name/" + country_request).json()              
print(rawdata[0]['name']['common'] + rawdata[0]['cca2'])
print(rawdata[0]['currencies'])
# print(rawdata[0]['currencies']['AUD']['symbol'])

for cur in rawdata[0]['currencies']:
    print(cur + ": " + rawdata[0]['currencies'][cur]['name'])