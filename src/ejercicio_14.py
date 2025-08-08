# Ejercicio 14: Sistema de Votación
# Crea una función que simule un sistema de votación. Usa un conjunto para almacenar los votos únicos y un ciclo while para permitir que múltiples usuarios voten. 
# Al final, muestra los candidatos que recibieron votos.

def sistemea_votacion():
    votos = set()
    while True:
        voto = input("Ingrese el nombre del candidato al que desea votar (o 'salir' para terminar): ")
        if voto.lower() == 'salir':
            break
        votos.add(voto)
    print("Candidatos que recibieron votos:")
    for candidato in votos:
        print(candidato)
        
sistemea_votacion()