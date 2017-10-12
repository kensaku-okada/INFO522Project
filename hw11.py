# Danielle, Kensaku, Alexander, Adrianna, Eddie
from requests import Session
import json
session = Session()

#list to hold data
latLngList = []

#known working keys
observations = ['2', '643', '10023']

#loop to iterate through observation keys and pull data from given url
#data is stored as a list in the latlong list
for i in observations:
    response = session.get('http://inaturalist.org/observations/' + str(i)+'.json')
    jsonVar = json.loads(response.text)
    latLngList.append([jsonVar["latitude"], jsonVar["longitude"]])

print(latLngList)
# print (response)