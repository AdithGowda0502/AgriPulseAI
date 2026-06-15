import pyodbc

server = 'localhost\\SQLEXPRESS'
database = 'AgriPulseDB'

conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO WeatherData
(City, Temperature, Humidity, WeatherCondition)
VALUES (?, ?, ?, ?)
""",
("Bangalore", 28.5, 72, "Cloudy"))

conn.commit()

print("✅ Weather data inserted successfully!")

conn.close()