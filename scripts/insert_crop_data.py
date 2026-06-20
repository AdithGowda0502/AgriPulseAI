import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AgriPulseDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

crop_records = [
    ("Rice", "Kharif", "Karnataka", 4.5, 2500),
    ("Wheat", "Rabi", "Karnataka", 3.8, 2200),
    ("Maize", "Kharif", "Karnataka", 5.2, 1900),
    ("Sugarcane", "Annual", "Karnataka", 80.0, 350),
    ("Cotton", "Kharif", "Karnataka", 2.8, 7000)
]

for record in crop_records:
    cursor.execute("""
    INSERT INTO CropData
    (CropName, Season, StateName, ExpectedYield, MarketPrice)
    VALUES (?, ?, ?, ?, ?)
    """, record)

conn.commit()

print("✅ Crop data inserted successfully!")

conn.close()