# Ejercicio 4: Carrito de Compras
# Desarrolla una función que simule un carrito de compras. Usa una lista para almacenar productos y un ciclo while para mostrar
# un menú que permita agregar, eliminar, mostrar productos y calcular el total.

def carrito_de_compras():
    carrito = []
    precios = {}
    
    while True:
        print("\n--- Carrito de Compras ---\n")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Calcular total")
        print("5. Salir\n")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input(f"Ingrese el precio de {producto}: "))
            carrito.append(producto)
            precios[producto] = precio
            print(f"{producto} agregado al carrito.")
        
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a eliminar: ")
            if producto in carrito:
                carrito.remove(producto)
                del precios[producto]
                print(f"{producto} eliminado del carrito.")
            else:
                print(f"{producto} no se encuentra en el carrito.")
        
        elif opcion == '3':
            if not carrito:
                print("El carrito está vacío.")
            else:
                print("Productos en el carrito:")
                for prod in carrito:
                    print(f"- {prod}: ${precios[prod]:.2f}")
        
        elif opcion == '4':
            total = sum(precios[prod] for prod in carrito)
            print(f"Total del carrito: ${total:.2f}")
        
        elif opcion == '5':
            print("¡Gracias por tu compra!")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")
            
if __name__ == "__main__":
    carrito_de_compras()
