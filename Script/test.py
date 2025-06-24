import requests

COUNTRIES_URL = "https://restcountries.com/v3.1/"
country_request = input("Which country would you like to choose?: ")

rawdata = requests.get(COUNTRIES_URL + "name/" + country_request)
rawdatajson = requests.get(COUNTRIES_URL + "name/" + country_request).json()   
print("Country found: " + rawdata[0]['name']['common'])
print("Getting other countries in the region...")


byregion = requests.get(COUNTRIES_URL + "region/" + rawdata[0]['region'])
for country in byregion:
    countrydata = requests.get(COUNTRIES_URL + "name/" + country['name']['common'])
    print(countrydata[0]['name']['common'])
    print("Capital: " + countrydata[0]['capital'][0])
    print("Population: " + str(countrydata[0]['population']))
    print("Area: " + str(countrydata[0]['area']) + " km²")
    print("Languages: " + ", ".join(countrydata[0]['languages'].values()))