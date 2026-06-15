import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m,relative_humidity_2m"

response = requests.get(url)

data = response.json()

print("Temperature:", data["current"]["temperature_2m"])
print("Humidity:", data["current"]["relative_humidity_2m"])