import requests

# set up the parameters we want to pass to the api
# this is the latitude and longitude of New York City
parameters = {"lat": 40.71, "lon": -74}

# make a get request to get the latest position of the international space station
# from the opennotify api with the parameters
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# print the content of the response (the data the server returned)
print(response.content)

