
def sistema_calificaciones():
    print("Por favor ingrese sus calificaciones. Escribe 'fin' para terminar.")
    notas = []
    
    while True:
        
        entrada = input(f"calificacón #{""} {len(notas) + 1}: ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 5:
                notas.append(nota)
            else:
                print("Por favor, ingrese una calificación entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido o 'fin' para terminar.")
    
    if not notas:
        print("No se ingresaron calificaciones.")
        return
    
    promedio = sum(notas) / len(notas)
    nota_mas_alta = max(notas)
    nota_mas_baja = min(notas)
    
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {nota_mas_alta:.2f}")
    print(f"Nota más baja: {nota_mas_baja:.2f}")

sistema_calificaciones()