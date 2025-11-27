from Connection.db import obtener_conexion

def crear_tabla_cliente():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
                   CREATE TABLE Cliente (
                       id_cliente INT PRIMARY KEY,
                       nombre VARCHAR(50) NOT NULL,
                       correo VARCHAR(100) NOT NULL,
                       telefono VARCHAR(20) NOT NULL
                   )
                   """)
    conexion.commit()
    conexion.close()
    print("Tabla 'Cliente' creada exitosamente.")