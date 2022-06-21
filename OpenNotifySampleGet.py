# This code written and modified from a dataquest tutorial on API interaction at:
# https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json
from datetime import datetime

def jprint(obj):
    #create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Dictionary of parameters to the iss-pass API to lookup
#Adjust this for different locations, currently Houston
parameters = {
    "lat": 29.76,
    "lon": -95.36
}

#Who and a count of people in space (ISS)
#response = requests.get("http://api.open-notify.org/astros.json")
#jprint(response.json())

#Returns time until ISS is above a location
#Specified in dictionary
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
jprint(response.json())

#Extract just the pass times
#You could probably commment out the above print to limit repeated text
pass_times = response.json()['response']
jprint(pass_times)

#Use a loop to extract risetimes as a list
risetimes = []
for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
    print(risetimes)

#Use a loop to convert timestamps to human readable format
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
