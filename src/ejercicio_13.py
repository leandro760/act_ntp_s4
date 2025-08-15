def conjuntos():
    numeros_pares = set()
    for i in range(2, 21):
        if i % 2 == 0:
            numeros_pares.add(i)

    multiplos_tres = set()
    for i in range(3, 31):
        if i % 3 == 0:
            multiplos_tres.add(i)

    print(f"Números pares del 2 al 20: {numeros_pares}")
    print(f"Múltiplos de 3 del 3 al 30: {multiplos_tres}")

    union = numeros_pares.union(multiplos_tres) 
    interseccion = numeros_pares.intersection(multiplos_tres)
    diferencia = numeros_pares.difference(multiplos_tres)
    diferencia_inversa = multiplos_tres.difference(numeros_pares)
    simetrica = numeros_pares.symmetric_difference(multiplos_tres) 
    
    print("\nOperaciones entre los conjuntos:")
    print(f"Unión: {union}")
    print(f"Intersección: {interseccion}")
    print(f"Diferencia (pares - múltiplos de 3): {diferencia}")
    print(f"Diferencia inversa (múltiplos de 3 - pares): {diferencia_inversa}")
    print(f"Diferencia simétrica: {simetrica}")

conjuntos()
    
    



     