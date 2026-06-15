import pyodbc

server = 'localhost\\SQLEXPRESS'
database = 'AgriPulseDB'

conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

print("✅ Connected to SQL Server successfully!")

conn.close()