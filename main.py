from views.vistaUsuarios import usuarios
from views.vistaTienda import tienda

def menu():
    while True:
        
        print("\n ========= VISTA PRINCIPAL ==========")
        print("1. Gestión de clientes")
        print("2. Gestion de tienda")
        print("3. Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        match opcion:
            case 1:
                usuarios()
            case 2:
                tienda()
            case 3:
                break
            case _:
                print("opcion incorrecta")

if __name__=="__main__":
    menu()
