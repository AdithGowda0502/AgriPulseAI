import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AgriPulseDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Get latest temperature
cursor.execute("""
SELECT TOP 1 Temperature
FROM WeatherData
ORDER BY WeatherID DESC
""")

latest_temp = cursor.fetchone()[0]

print(f"\nCurrent Temperature: {latest_temp} °C\n")

# Clear old recommendations
cursor.execute("DELETE FROM RecommendedCrops")

# Find suitable crops
cursor.execute("""
SELECT CropName, Recommendation
FROM CropRecommendation
WHERE ? BETWEEN TemperatureMin AND TemperatureMax
""", latest_temp)

results = cursor.fetchall()

print("Recommended Crops:\n")

for row in results:
    crop_name = row[0]
    recommendation = row[1]

    print(f"✓ {crop_name} - {recommendation}")

    cursor.execute("""
    INSERT INTO RecommendedCrops
    (CropName, Recommendation, Temperature)
    VALUES (?, ?, ?)
    """,
    (crop_name, recommendation, latest_temp))

conn.commit()

print("\n✅ Recommendations saved to SQL Server!")

conn.close()