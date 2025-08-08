# Ejercicio 17: Contador de Palabras
# Desarrolla una función que reciba una frase y use un ciclo for para crear un diccionario que cuente la frecuencia de cada palabra.
# Ignora mayúsculas/minúsculas y muestra las palabras ordenadas por frecuencia.

def contar_palabras(frase):
      # Dividir la frase en palabras
    palabras = frase.split()
    
    # Ignorar mayúsculas y minúsculas
    palabras = [palabra.lower() for palabra in palabras]


    # Crear un diccionario para contar las palabras
    contador = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    # Ordenar el diccionario por frecuencia
    contador_ordenado = dict(sorted(contador.items(), key=lambda item: item[1], reverse=True))
    
    return contador_ordenado

# Ejemplo de uso
frase = "Bienvenido a Python, hola mundo! Hola Python, Python es genial. Hola!"

# Llamada a la función y mostrar el resultado
resultado = contar_palabras(frase)

# Mostrar el resultado
print(resultado)  