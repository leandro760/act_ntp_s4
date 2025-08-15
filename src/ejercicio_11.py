def operaciones_conjuntos(lista1, lista2):
    
    conjunto1 = set()
    for elemento in lista1:
        conjunto1.add(elemento)
    
    conjunto2 = set()
    for elemento in lista2:
        conjunto2.add(elemento)

    union = conjunto1 | conjunto2
    interseccion = conjunto1 & conjunto2
    diferencia = conjunto1 - conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2
    
    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia (Conjunto 1 - Conjunto 2):", diferencia)
    print("Diferencia Simétrica:", diferencia_simetrica)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


operaciones_conjuntos(lista1, lista2)