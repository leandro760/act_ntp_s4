def palabras():
    print("Por favor ingrese palabras. Escribe 'salir' para terminar.")
    unicas = set()
    repetidas = set()

    while True:
        palabra = input(f"Palabra #{len(unicas) + len(repetidas) + 1}: ")
        if palabra.lower() == 'salir':
            break
        if palabra in unicas:
            repetidas.add(palabra)
        else:
            unicas.add(palabra)

    if not unicas:
        print("No se ingresaron palabras.")
        return  

    print(f"Palabras únicas ingresadas: {len(unicas)}")
    if repetidas:
        print(f"Palabras repetidas: {', '.join(repetidas)}")    
    else:
        print("No se ingresaron palabras repetidas.")

palabras()



    

