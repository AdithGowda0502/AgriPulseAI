import requests
import pyodbc

# Open-Meteo API
url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=12.97"
    "&longitude=77.59"
    "&current=temperature_2m,relative_humidity_2m,weather_code"
)

# Fetch data
response = requests.get(url)
data = response.json()

# Extract values
temperature = data["current"]["temperature_2m"]
humidity = data["current"]["relative_humidity_2m"]
weather_code = data["current"]["weather_code"]

# Weather code mapping
weather_map = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Heavy Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
    96: "Thunderstorm with Hail",
    99: "Severe Thunderstorm"
}

weather_condition = weather_map.get(weather_code, "Unknown")

print(f"Temperature: {temperature} °C")
print(f"Humidity: {humidity} %")
print(f"Weather: {weather_condition}")

# SQL Server Connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AgriPulseDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Insert data
cursor.execute("""
INSERT INTO WeatherData
(City, Temperature, Humidity, WeatherCondition)
VALUES (?, ?, ?, ?)
""",
(
    "Bangalore",
    temperature,
    humidity,
    weather_condition
))

conn.commit()

print("✅ Live weather inserted into SQL Server!")

conn.close()