from Connection.db import obtener_conexion

def crear_tabla_venta():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
                   CREATE TABLE venta(
                       id_venta INT PRIMARY KEY IDENTITY(1,1),
                       id_cliente INT,
                       id_producto INT,
                       id_vendedor INT,
                       cantidad INT NOT NULL CHECK (cantidad > 0),
                       total MONEY,
                       FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                       FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
                       FOREIGN KEY (id_vendedor) REFERENCES vendedor(id_vendedor)
                   )
                   """)
    conexion.commit()
    cursor.close()
    print("Tabla 'venta' creada exitosamente.")