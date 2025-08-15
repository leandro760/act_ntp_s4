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