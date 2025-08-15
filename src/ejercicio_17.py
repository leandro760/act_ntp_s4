

def contar_palabras(frase):
    palabras = frase.split()
    palabras = [palabra.lower() for palabra in palabras]
    contador = {}
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    contador_ordenado = dict(sorted(contador.items(), key=lambda item: item[1], reverse=True))
    return contador_ordenado

frase = "Bienvenido a Python, hola mundo! Hola Python, Python es genial. Hola!"
resultado = contar_palabras(frase)

print(resultado)  