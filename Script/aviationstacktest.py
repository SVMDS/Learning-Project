import requests
import json

AVIATIONSTACK_URL = "http://api.aviationstack.com/v1/"
aviationstackapikey = '' # REPLACE WITH YOUR AVIATIONSTACK API KEY

# UNCOMMENT TO GET FRESH DATA. SAVING TO FILE TO AVOID REPEATED REQUESTS THAT USE API QUOTA
# response = requests.get(f"{AVIATIONSTACK_URL}flights?access_key={aviationstackapikey}&flight_status=active").json()
# with open("aviationstack_flights.json", "w") as file:
#     json.dump(response, file, indent=4)

# LOAD DATA FROM SAVED FILE TO PRACTICE QUERIES
with open("aviationstack_flights.json", "r") as file:
    activeflights = json.load(file)

# TAKE THE LIST OF ACTIVE FLIGHTS AND PICK ONE AT RANDOM

# FOR THAT FLIGHT, GET THE DETAILS OF THE AIRPORTs USING THE IATA CODE AND THE AVIATIONSTACK AIRPORTS API 
# (Seems undocumented but can pass iata_code as a parameter in the URL like below)
# https://api.aviationstack.com/v1/airports?access_key=...&iata_code=AKL

# USING THE INFORMATION ABOUT THE AIRPORTS, USE THE COUNTRIES API TO GET THE POPULATION, CURRENCY, AND CAPITAL OF THE DEPATURE AND ARRIVAL COUNTRIES

# DISPLAY THE FOLLOWING INFORMATION:
# THESE FIELDS WILL COME FROM MARRYING THE FLIGHT DATA WITH THE AIRPORT DATA AND COUNTRY DATA WHICH IS USEFUL TO PRACTICE
    # depature country
    # depature country population
    # depature country capital
    # depature country region
    # depature country languages
    # depature country currency
    # departure airport name
    # arrival country
    # arrival country population
    # arrival country capital
    # arrival country region
    # arrival country languages
    # arrival country currency
    # arrival airport name
# THIS WILL HELP DEAL WITH SOME DATETIME FORMATS, FIGURING OUT DIFFERENCE BETWEEN TIMES IS A FAIRLY COMMON TASK
    # total flight estimated duration (ignoring delays)
# A LITTLE BIT OF MATH
    # time difference between departure and arrival locations
# A LOT OF MATH, TO DO THIS IT SEEMS LIKE THERE ARE SOME EQUATIONS NEEDED WHICH CAN BE FOUND ONLINE
    # distance between departure and arrival airports measured in kilometers and miles (STRETCH GOAL)
# KNOWING THE CURRENCY EXCHANGE RATE IS NOT A DATASOURCE WE CURRENTLY HAVE, WILL NEED TO SOURCE THIS FROM ANOTHER API AND CALCULATE
    # exchange rate from departure country to arrival country currency (STRETCH GOAL)

# ONCE DATA IS DISPLAYED AND FLOWING WELL, REFACTOR THE CODE TO USE FUNCTIONS TO MAKE IT MORE READABLE AND MAINTAINABLE

# THINK ABOUT ANYTHING THAT IS REPEATED AND COULD BE MADE INTO A FUNCTION, OR LOGIC WHICH COULD BE WRAPPED IN A FUNCTION

# THINK ABOUT HOW TO HANDLE ERRORS AND EXCEPTIONS, SUCH AS IF A COUNTRY OR AIRPORT IS NOT FOUND

# UPDATE THE SCRIPT TO USE THE AVIATIONSTACK FLIGHTS API TO GET AN ACTIVE FLIGHT AND DISPLAY THE INFORMATION, RATHER THAN USING THE SAVED FILE