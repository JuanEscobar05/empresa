from Crd.crudProducto import crear_producto, listar_producto, actualizar_producto, eliminar_producto

def producto():
    while True:
        print("\n ========== PRODUCTO ==========")
        print("1. Crear Producto")
        print("2. ver producto")
        print("3. actualziar producto")
        print("4. eliminar producto")
        print("5. salir al menú principal")
        
        opcion = int(input("Ingrese una opción: "))
        
        match opcion:
            case 1:
                nombre = input("ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del prodcuto: "))
                stock = int(input("Ingrese el stock: "))
                crear_producto(nombre, precio, stock)
            case 2:
                listar_producto()
            case 3:
                id_producto = int(input("ingrese el id del producto: "))
                precio = float(input("Ingrese el nuevo valor: "))
                stock = int(input("Ingrese el nuevo stock: "))
                actualizar_producto(id_producto,precio,stock)
            case 4:
                id_producto = int(input("Ingrese el id del producto a eliminar: "))
                eliminar_producto(id_producto)
            case 5:
                break
            case _:
                print("opcion incorrecta")
                