from Connection.db import obtener_conexion

def crear_vendedor(id_vendedor, nombre, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Vendedor (id_vendedor, nombre, correo) VALUES (?,?,?)",
                   (id_vendedor, nombre, correo))
    conexion.commit()
    conexion.close()
    print("vendedor registrado con exito")

def listar_vendedor ():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Vendedor")
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def actualizar_vendedor(id_vendedor, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Vendedor SET correo = ? WHERE id_vendedor = ? ",
                   (correo, id_vendedor))
    conexion.commit()
    conexion.close()
    print("vendedor actualizado")

def eliminar_vendedor(id_vendedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Vendedor WHERE id_vendedor = ?",
                   (id_vendedor))
    conexion.commit()
    conexion.close()
    print("vendedor eliminado exitosamente")