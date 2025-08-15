def eliminar_duplicados():
    numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]  
    numeros_unicos = set()  

    for numero in numeros:
        numeros_unicos.add(numero)  

    numeros = list(numeros) 
    numeros_unicos = list(numeros_unicos)
    cantidad_original = len(numeros)
    cantidad_unicos = len(numeros_unicos)
    cantidad_duplicados = cantidad_original - cantidad_unicos

    print(f"Números originales: {numeros}")
    print(f"Números únicos: {numeros_unicos}")
    print(f"Cantidad original: {cantidad_original}")
    print(f"Cantidad de números únicos: {cantidad_unicos}")
    print(f"Cantidad de duplicados: {cantidad_duplicados}")
   
eliminar_duplicados()


