import pyodbc

def obtener_conexion():
    
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=DESKTOP-I8M40F5\\SQLEXPRESS;'
        'DATABASE=Tienda;'
        'UID=sa;'
        'PWD=Juan1032;'
        'TrustServerCertificate=yes;'
    )
    
    return conexion