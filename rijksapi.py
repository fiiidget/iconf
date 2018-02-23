import requests
import json
import urllib3
#  jmkt4GYt is the key
response = requests.get("https://www.rijksmuseum.nl/api/usersets/1774320--ocarine/collections/jewelry?key=jmkt4GYt&format=json")

# Print the content of the response.
print(response)
# parameters = {"lat": 37.78, "lon": -122.41}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
#
# # Get the response data as a python object.  Verify that it's a dictionary.
# data = response.json()
# print(type(data))
# print(data)

https://www.rijksmuseum.nl/api/collection/usersets/{userid}-{collection name}?key=jmkt4GYt&format=json
