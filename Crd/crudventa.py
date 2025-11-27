from Connection.db import obtener_conexion

def crear_venta(id_cliente, id_producto, id_vendedor, cantidad):
    """Crea una nueva venta y calcula el total automáticamente"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        # Obtener el precio y stock del producto
        cursor.execute("SELECT precio, stock FROM Producto WHERE id_producto = ?", (id_producto,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("El producto no existe")
            conexion.close()
            return
        
        precio, stock = resultado
        
        # Verificar si hay stock disponible
        if stock <= 0:
            print("⚠️  No hay producto disponible")
            conexion.close()
            return
        
        # Verificar si la cantidad solicitada es mayor al stock
        if cantidad > stock:
            print(f"⚠️  Stock insuficiente. Stock disponible: {stock}, Cantidad solicitada: {cantidad}")
            conexion.close()
            return
        
        total = precio * cantidad
        
        # Insertar la venta
        cursor.execute("""INSERT INTO venta (id_cliente, id_producto, id_vendedor, cantidad, total) 
                         VALUES (?,?,?,?,?)""",
                       (id_cliente, id_producto, id_vendedor, cantidad, total))
        
        # Actualizar el stock del producto (restar cantidad vendida)
        nuevo_stock = stock - cantidad
        cursor.execute("UPDATE Producto SET stock = ? WHERE id_producto = ?",
                       (nuevo_stock, id_producto))
        
        conexion.commit()
        print(f"✓ Venta registrada exitosamente. Total: ${total}")
        print(f"  Stock restante del producto: {nuevo_stock}")
        
        # Si el stock llega a cero, mostrar advertencia
        if nuevo_stock == 0:
            print("⚠️  ADVERTENCIA: El producto ha alcanzado stock cero")
    except Exception as e:
        print(f"Error al crear venta: {e}")
    finally:
        conexion.close()

def listar_ventas():
    """Lista todas las ventas con información del cliente, producto, vendedor y total"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("""
            SELECT 
                v.id_venta,
                c.id_cliente,
                c.nombre AS nombre_cliente,
                p.nombre AS nombre_producto,
                vd.nombre AS nombre_vendedor,
                v.cantidad,
                v.total
            FROM venta v
            INNER JOIN Cliente c ON v.id_cliente = c.id_cliente
            INNER JOIN Producto p ON v.id_producto = p.id_producto
            INNER JOIN vendedor vd ON v.id_vendedor = vd.id_vendedor
            ORDER BY v.id_venta DESC
        """)
        
        ventas = cursor.fetchall()
        
        if not ventas:
            print("No hay ventas registradas")
            return
        
        print("\n" + "="*120)
        print(f"{'ID':<5} {'Cliente ID':<12} {'Cliente':<20} {'Producto':<20} {'Vendedor':<20} {'Cantidad':<10} {'Total':<12}")
        print("="*120)
        
        for venta in ventas:
            id_venta, id_cliente, nombre_cliente, nombre_producto, nombre_vendedor, cantidad, total = venta
            print(f"{id_venta:<5} {id_cliente:<12} {nombre_cliente:<20} {nombre_producto:<20} {nombre_vendedor:<20} {cantidad:<10} ${total:<11.2f}")
        
        print("="*120 + "\n")
    except Exception as e:
        print(f"Error al listar ventas: {e}")
    finally:
        conexion.close()

def actualizar_venta(id_venta, cantidad):
    """Actualiza la cantidad y recalcula el total de una venta"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        # Obtener el producto_id y precio de la venta actual
        cursor.execute("SELECT id_producto FROM venta WHERE id_venta = ?", (id_venta,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("La venta no existe")
            conexion.close()
            return
        
        id_producto = resultado[0]
        
        # Obtener el precio del producto
        cursor.execute("SELECT precio FROM Producto WHERE id_producto = ?", (id_producto,))
        precio_resultado = cursor.fetchone()
        precio = precio_resultado[0]
        
        # Calcular nuevo total
        nuevo_total = precio * cantidad
        
        # Actualizar la venta
        cursor.execute("""UPDATE venta SET cantidad = ?, total = ? WHERE id_venta = ?""",
                       (cantidad, nuevo_total, id_venta))
        conexion.commit()
        print(f"Venta actualizada. Nueva cantidad: {cantidad}, Nuevo total: ${nuevo_total}")
    except Exception as e:
        print(f"Error al actualizar venta: {e}")
    finally:
        conexion.close()

def eliminar_venta(id_venta):
    """Elimina una venta"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("DELETE FROM venta WHERE id_venta = ?", (id_venta,))
        conexion.commit()
        print("Venta eliminada correctamente")
    except Exception as e:
        print(f"Error al eliminar venta: {e}")
    finally:
        conexion.close()

def buscar_venta(id_venta):
    """Busca una venta específica por ID"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("""
            SELECT 
                v.id_venta,
                c.id_cliente,
                c.nombre AS nombre_cliente,
                p.nombre AS nombre_producto,
                vd.nombre AS nombre_vendedor,
                v.cantidad,
                v.total
            FROM venta v
            INNER JOIN Cliente c ON v.id_cliente = c.id_cliente
            INNER JOIN Producto p ON v.id_producto = p.id_producto
            INNER JOIN vendedor vd ON v.id_vendedor = vd.id_vendedor
            WHERE v.id_venta = ?
        """, (id_venta,))
        
        venta = cursor.fetchone()
        
        if venta is None:
            print("La venta no existe")
            return
        
        id_venta, id_cliente, nombre_cliente, nombre_producto, nombre_vendedor, cantidad, total = venta
        print("\n" + "="*80)
        print(f"ID Venta: {id_venta}")
        print(f"Cliente ID: {id_cliente} - Nombre: {nombre_cliente}")
        print(f"Producto: {nombre_producto}")
        print(f"Vendedor: {nombre_vendedor}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: ${total:.2f}")
        print("="*80 + "\n")
    except Exception as e:
        print(f"Error al buscar venta: {e}")
    finally:
        conexion.close()
