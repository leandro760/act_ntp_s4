# Ejercicio 6: Coordenadas Aleatorias
# Crea una función que genere una tupla con las coordenadas (x, y) de 10 puntos aleatorios. 
# Usa un ciclo for para calcular cuáles puntos están dentro de un círculo de radio 5 centrado en el origen.
      
import random

def coordenadas(numero_puntos=10, radio=5.0, rango_aleatorio=10.0):
 
  
    puntos = ()
    puntos_dentro = []

    for _ in range(numero_puntos):
        x = random.uniform(-rango_aleatorio, rango_aleatorio)
        y = random.uniform(-rango_aleatorio, rango_aleatorio)
        puntos += ((x, y),)

        if x*x + y*y <= radio*radio:
            puntos_dentro.append((x, y))

    return puntos, tuple(puntos_dentro)

if __name__ == "__main__":
    todos, dentro = coordenadas()

    print("Puntos generados (tupla de 10):")
    for i, p in enumerate(todos, 1):
        estado = "dentro" if p in dentro else "fuera"
        print(f" Punto {i}: {p} -> {estado}")

    print("\nListado final (tupla) de puntos dentro del círculo:")
    print(dentro)
      


