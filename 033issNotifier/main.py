import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=url)

# response code returned - 200
# 1XX - hold on / something is happening
# 2XX - successful / here you go
# 3XX - no permission / go away
# 4XX - doesn't exist / you screwed up
# 5XX - server screwed up
status = response.status_code

# raise exceptions for error codes
response.raise_for_status()

data = response.json()["iss_position"]
longitude = data["longitude"]
latitude = data["latitude"]

iss_possition = (latitude, longitude)