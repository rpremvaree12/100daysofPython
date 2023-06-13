import requests
import geocoder
g = geocoder.ip('me')

url="https://api.sunrise-sunset.org/json"

# current lat / long
lat = g.latlng[0]
lng = g.latlng[1]

url += f"?lat={lat}&lng={lng}"
response = requests.get(url=url)
response.raise_for_status()
data = response.json()["results"]

sunrise = data["sunrise"]
sunset = data["sunset"]
day_length = data["day_length"]

print(lat)
print(lng)