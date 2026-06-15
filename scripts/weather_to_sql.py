import requests
import pyodbc

# Get live weather
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m,relative_humidity_2m"

data = requests.get(url).json()

temperature = data["current"]["temperature_2m"]
humidity = data["current"]["relative_humidity_2m"]

# Connect SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AgriPulseDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO WeatherData
(City, Temperature, Humidity, WeatherCondition)
VALUES (?, ?, ?, ?)
""",
("Bangalore", temperature, humidity, "Live API"))

conn.commit()

print("✅ Live weather inserted into SQL Server!")

conn.close()
