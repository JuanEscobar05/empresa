from Connection.db import obtener_conexion

def crear_tabla_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
                   CREATE TABLE Producto(
                       id_producto INT PRIMARY KEY IDENTITY(1,1),
                       nombre VARCHAR(100) NOT NULL,
                       precio MONEY NOT NULL,
                       stock INT NOT NULL
                   )
                   """)
    conexion.commit()
    cursor.close()
    print("Tabla 'Producto' creada exitosamente.")