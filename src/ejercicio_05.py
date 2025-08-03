# Ejercicio 5: Búsqueda de Palabras
# Implementa una función que reciba una lista de palabras y use ciclos anidados para encontrar y 
# devolver todas las palabras que contienen una letra específica ingresada por el usuario.

def buscar_palabras(palabras):
    letra = input("Ingrese una letra para buscar en las palabras: ").lower()
    palabras_encontradas = []

    for palabra in palabras:
        for caracter in palabra:
            if caracter.lower() == letra:
                palabras_encontradas.append(palabra)
                break  

    if palabras_encontradas:
        print(f"Palabras que contienen la letra '{letra}': {', '.join(palabras_encontradas)}")
    else:
        print(f"No se encontraron palabras que contengan la letra '{letra}'.")

if __name__ == "__main__":
    lista_palabras = ["brasil", "programación", "vegueta", "desarrollo", "zapato"]
    buscar_palabras(lista_palabras)