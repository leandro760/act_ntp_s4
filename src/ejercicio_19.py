# Ejercicio 19: Gestión de Calificaciones
# Crea una función que gestione las calificaciones de estudiantes. Usa un diccionario donde la clave sea el nombre del estudiante 
# y el valor una lista de calificaciones. Implementa funciones para agregar estudiantes, agregar calificaciones y calcular promedios.

def gestionar_calificaciones():
    calificaciones = {}

    # Ciclo para mostrar el menú y gestionar las calificaciones
    while True:
        print("\nMenú de Gestión de Calificaciones:\n")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Mostrar calificaciones")
        print("5. Salir\n")
        
        # Solicitar opción al usuario
        opcion = input("Seleccione una opción: ")

        # Procesar la opción seleccionada
        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre not in calificaciones:
                calificaciones[nombre] = []
                print(f"Estudiante {nombre} agregado.")
            else:
                print(f"El estudiante {nombre} ya existe.")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre in calificaciones:
                calificacion = float(input("Ingrese la calificación: "))
                calificaciones[nombre].append(calificacion)
                print(f"Calificación {calificacion} agregada para {nombre}.")
            else:
                print(f"El estudiante {nombre} no existe.")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre in calificaciones and calificaciones[nombre]:
                promedio = sum(calificaciones[nombre]) / len(calificaciones[nombre])
                print(f"El promedio de {nombre} es {promedio:.2f}.")
            else:
                print(f"El estudiante {nombre} no tiene calificaciones.")

        elif opcion == '4':
            for estudiante, notas in calificaciones.items():
                print(f"{estudiante}: {notas}")

        elif opcion == '5':
            print("Saliendo del programa.")
            break
        # Si la opción no es válida, se muestra un mensaje de error
        else:
            print("Opción no válida, intente nuevamente.")

        # llamar a la función recursivamente para mostrar el menú nuevamente

gestionar_calificaciones()