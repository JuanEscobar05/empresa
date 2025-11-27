from Crd.crudventa import crear_venta, listar_ventas, actualizar_venta, eliminar_venta, buscar_venta

def venta():
    while True:
        print("\n ========== VENTAS ==========")
        print("1. Crear Venta")
        print("2. listar Ventas")
        print("3. Actualizar ventas")
        print("4. Eliminar ventas")
        print("5. buscar_ventas")
        print("6. salir al menú principal")
        
        opcion = int(input("Ingre la opción: "))
        
        match opcion:
            case 1:
                id_cliente = int(input("Ingrese el id del Cliente: "))
                id_producto = int(input("Ingrese el id del producto: "))
                id_vendedor = int(input("Ingrese el id del vendedor: "))
                cantidad = int(input("Ingrese la cantidad de producto: "))
                crear_venta(id_cliente, id_producto, id_vendedor, cantidad)
            case 2:
                listar_ventas()
            case 3:
                id_venta = int(input("Ingrese el id de la venta: "))
                cantidad = int(input("Ingrese la nueva cantidad: "))
                actualizar_venta(id_venta, cantidad)
            case 4:
                id_venta = int(input("Ingrese el id de la venta que desea eliminar: "))
                eliminar_venta(id_venta)
            case 5:
                id_venta = int(input("Ingrese el id de la venta a buscar: "))
                buscar_venta(id_venta)
            case 6:
                break
            case _:
                input("opcion incorrecta")