from Crd.crudVendedor import crear_vendedor, listar_vendedor, actualizar_vendedor, eliminar_vendedor

def vendedor():
    while True:
        print("\n ========== VENDEDOR ==========")
        print("1. Crear vendedor")
        print("2. listar vendedr")
        print("3. actualzar vendedor")
        print("4. eliminar vendedor")
        print("5. salir al menú principal")
        
        opcion = int(input("Ingrese una opción: "))
        
        match opcion:
            case 1:
                id_vendedor = int(input("Ingrese el ID del vendedor: "))
                nombre = input("ingrese el nombre del vendedor: ")
                correo = input("ingrese el correo del vendedor: ")
                crear_vendedor(id_vendedor, nombre, correo)
            case 2:
                listar_vendedor()
            case 3:
                id_vendedor = int(input("Ingrese el ID del vendedor: "))
                correo = input("ingrese el nuevo correo del vendedor: ")
                actualizar_vendedor(id_vendedor,correo)
            case 4:
                id_vendedor = int(input("Ingrese el ID del vendedor: "))
                eliminar_vendedor(id_vendedor)
            case 5:
                break
            case _:
                print("opción incorrecta")