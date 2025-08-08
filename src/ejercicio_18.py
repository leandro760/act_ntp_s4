# Ejercicio 18: Agenda Telefónica
# Implementa una función que simule una agenda telefónica usando un diccionario. Usa un ciclo while para mostrar un menú
# que permita agregar contactos, buscar por nombre, mostrar todos los contactos y eliminar contactos.

#comentar en español
# Función para gestionar una agenda telefónica
def agenda_telefonica():
    agenda = {}
    
    # Ciclo para mostrar el menú y realizar acciones
    while True:
        print("\n--- Agenda Telefónica ---\n")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir\n")
        
        # Solicitar opción al usuario
        opcion = input("Selecciona una opción: ")
        
        # Procesar la opción seleccionada
        # Agregar contacto
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado.")
        
        # Buscar contacto por nombre
        elif opcion == '2':
            nombre = input("Ingrese el nombre a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado.")
        
        # Mostrar todos los contactos
        elif opcion == '3':
            if agenda:
                print("\nContactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos en la agenda.")
        
        # Eliminar contacto
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print(f"Contacto {nombre} no encontrado.")
        
        # Salir del programa
        elif opcion == '5':
            print("Saliendo de la agenda telefónica.")
            break
        
        # Opción no válida
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Llamar a la función.
agenda_telefonica()