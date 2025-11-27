from views.vistaProducto import producto
from views.vistaVendedor import vendedor
from views.vistaventa import venta

def tienda():
    while True:
         print ("\n===== GESTIÓN DE Tienda ===== ")
         print("1. Productos")
         print("2. vendedores")
         print("3. ventas")
         print("4. Volver al menú principal")
         
         opcion = int(input("Ingrese la Opción: "))
         
         match opcion:
             case 1:
                 producto()
             case 2:
                 vendedor()
             case 3:
                 venta()
             case 4:
                 break
             case _:
                 print("Opcion incorrecta")
             