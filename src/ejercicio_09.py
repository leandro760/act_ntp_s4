import math

def distacia_total(puntos):

    total = 0.0

    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total += distancia
    return total

puntos = [
    (0, 0), 
    (3, 4), 
    (6, 8), 
    (9, 12)
]

print("Distancia total recorrida:", distacia_total(puntos))



      
