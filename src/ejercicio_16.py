# Ejercicio 16: Inventario de Productos
# Crea una función que simule un inventario de productos. Usa un diccionario para almacenar producto:cantidad y un ciclo while para mostrar un menú que permita agregar,
# actualizar, eliminar productos y mostrar el inventario completo.

def inventario_productos():
    inventario = {}

    while True:
        print("\nMenú de Inventario:\n")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario completo")
        print("5. Salir\n")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario[producto] = inventario.get(producto, 0) + cantidad
            print(f"Producto '{producto}' agregado con cantidad {cantidad}.")

        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a actualizar: ")
            if producto in inventario:
                cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                inventario[producto] = cantidad
                print(f"Producto '{producto}' actualizado a cantidad {cantidad}.")
            else:
                print(f"Producto '{producto}' no encontrado en el inventario.")

        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a eliminar: ")
            if producto in inventario:
                del inventario[producto]
                print(f"Producto '{producto}' eliminado del inventario.")
            else:
                print(f"Producto '{producto}' no encontrado en el inventario.")

        elif opcion == '4':
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("Inventario completo:")
                for prod, cant in inventario.items():
                    print(f"{prod}: {cant}")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

inventario_productos()


   