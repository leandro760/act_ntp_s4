def agenda_telefonica():
    agenda = {}
    
    while True:
        print("\n--- Agenda Telefónica ---\n")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir\n")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado.")
        elif opcion == '3':
            if agenda:
                print("\nContactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos en la agenda.")
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print(f"Contacto {nombre} no encontrado.")
        elif opcion == '5':
            print("Saliendo de la agenda telefónica.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

agenda_telefonica()