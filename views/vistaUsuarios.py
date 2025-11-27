from Crd.crudCliente import crear_cliente, listar_cliente, actualizar_cliente, eliminar_cliente

def usuarios ():
    while True:
        print ("\n===== GESTIÓN DE CLIENTES ===== ")
        print("1. Crear Cliente")
        print("2. Leer Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al menú principal")
        
        opcion = int(input("Seleccione una opción: "))
        
        match opcion:
            case 1:
                id_cliente = int(input("Ingrese el id del cliente: "))
                nombre = input("Ingrese el nombre completo del cliente: ")
                correo = input("Ingrese el correo del cliente: ")
                telefono = input("Ingrese el telefono del cliente: ")
                crear_cliente(id_cliente, nombre, correo, telefono)
            case 2:
                listar_cliente()
            case 3:
                id_cliente = int(input("ingrese el id del cliente: "))
                correo = input("Ingrese el nuevo correo: ")
                telefono = input("Ingrese el nuevo telefono: ")
                actualizar_cliente(id_cliente, correo, telefono)
            case 4:
                id_cliente = int(input("Ingrese el id que desea eliminar: "))
                eliminar_cliente(id_cliente)
            case 5:
                break
            case _:
                 print("Opción no válida. Por favor, intente de nuevo.")