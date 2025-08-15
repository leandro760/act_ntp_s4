
def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
           pares.append(numero)
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros_pares(numeros))

