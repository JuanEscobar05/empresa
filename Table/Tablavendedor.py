from Connection.db import obtener_conexion

def crear_tabla_vendedor():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
                   CREATE TABLE vendedor(
                       id_vendedor INT PRIMARY KEY,
                       nombre VARCHAR(50) NOT NULL,
                       correo VARCHAR(100) NOT NULL
                   )
                   """)
    conexion.commit()
    conexion.close()
    print("Tabla 'vendedor' creada exitosamente.")