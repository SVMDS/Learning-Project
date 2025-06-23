import requests
import json
from collections import Counter
from collections import defaultdict

COUNTRIES_URL = "ttps://restcountries.com/v3.1/all?fields=name,region"
## Get all countries
response = requests.get("https://restcountries.com/v3.1/all")
data = response.json()
print("Status code:", response.status_code)
print("Sample content:", response.text[:300])

## Creating a dictionary where each region maps to a set of country names
if isinstance(data, list):
    countries_by_region = defaultdict(set)

    for country in data:
        region = country.get("region", "unknown")
        name = country.get("name", {}).get("common", "Unnamed")
        countries_by_region[region].add(name)

## Now print the number of countries in each region
    for region, countries in countries_by_region.items():
        print(f"{region}: {len(countries)} unique countries")

else:
    print("unexpected response format")

print("script has finished")



## old stuff that didnt work below
""" ## Count how many countries are in each unique region
region_counts = Counter(region)

## Ask which region you want to look at
query_request = input("Hi, which Continent would you like to choose?: ")

rawdata = requests.get(COUNTRIES_URL + "region/" + query_request).json()              

country_counter = input(f"Nice! You have selected {query_request.title()}. Would you like to know how many countries are in {query_request.title()}?")
if country_counter == "yes" or "y":
    for region, count in region_counts.items():
        print(f"{region}: {count} countries")
 """



""" print(rawdata[0]['name'] + rawdata[0]['cca2'])
print(rawdata[0]['currencies'])

for cur in rawdata[0]['currencies']:
    print(cur + ": " + rawdata[0]['currencies'][cur]['name'])   """