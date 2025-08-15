def registro_temperaturas():

    datos = {
        "Madrid": {"Lunes": 20, "Martes": 22, "Miércoles": 19, "Jueves": 21, "Viernes": 23, "Sábado": 25, "Domingo": 24},
        "Barcelona": {"Lunes": 23, "Martes": 24, "Miércoles": 22, "Jueves": 26, "Viernes": 27, "Sábado": 28, "Domingo": 29},
        "Valencia": {"Lunes": 25, "Martes": 26, "Miércoles": 24, "Jueves": 27, "Viernes": 28, "Sábado": 30, "Domingo": 31},
        "Sevilla": {"Lunes": 30, "Martes": 32, "Miércoles": 31, "Jueves": 33, "Viernes": 34, "Sábado": 35, "Domingo": 36},
    }

    estadisticas = {}

    for ciudad, temperaturas in datos.items():
        valores = list(temperaturas.values())
        promedio = sum(valores) / len(valores)  
        minimo = min(valores)
        maximo = max(valores)
        estadisticas[ciudad] = {
            "Promedio": promedio,
            "Mínimo": minimo,
            "Máximo": maximo
        }

    for ciudad, estad in estadisticas.items():
        print(f"Ciudad: {ciudad}")
        print(f"  Promedio: {estad['Promedio']:.2f}°C")
        print(f"  Mínimo: {estad['Mínimo']}°C")
        print(f"  Máximo: {estad['Máximo']}°C")
        print()

registro_temperaturas()