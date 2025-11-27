from Connection.db import obtener_conexion

def crear_cliente(id_cliente, nombre, correo, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("INSERT INTO Cliente (id_cliente, nombre, correo, telefono) VALUES (?,?,?,?)",
                   (id_cliente, nombre, correo, telefono))
    conexion.commit()
    conexion.close()
    print("Usuario registrado con exito")

def listar_cliente():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM Cliente")
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def actualizar_cliente(id_cliente, correo, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("UPDATE Cliente SET correo = ?, telefono = ? WHERE id_cliente = ?",
                   (correo, telefono, id_cliente))
    conexion.commit()
    conexion.close()
    print("usuario actualizado")

def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM Cliente WHERE id_cliente = ?",
                   (id_cliente))
    conexion.commit()
    conexion.close()
    print("Usuario eliminado correctamente")