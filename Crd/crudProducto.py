from Connection.db import obtener_conexion

def crear_producto(nombre, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Producto (nombre, precio, stock) VALUES (?,?,?)",
                   (nombre, precio, stock))
    conexion.commit()
    conexion.close()
    print("producto ingresado con exito")

def listar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Producto")
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def actualizar_producto(id_producto,precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Producto SET precio = ?, stock = ? WHERE id_producto = ?",
                   ( precio, stock, id_producto))
    conexion.commit()
    conexion.close()
    print("producto actualizado")

def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Producto WHERE id_producto = ?",
                   (id_producto))
    conexion.commit()
    conexion.cursor()
    print("producto borrado")