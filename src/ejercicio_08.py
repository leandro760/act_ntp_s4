# Ejercicio 8: Secuencia de Fibonacci
# Implementa una función que cree una tupla con los primeros 20 números de la secuencia de Fibonacci. 
# Usa un ciclo while para generar la secuencia y luego un ciclo for para mostrar solo los números impares.

def secuencia_fibonacci():
    fibonacci = []
    a, b = 0, 1
    while len(fibonacci) <= 20:
        fibonacci.append(a)
        a, b = b, a + b
    return tuple(fibonacci)

print("\nLos primeros 20 números de la secuencia de Fibonacci son: \n")
print(secuencia_fibonacci())

print("\nNúmeros impares en la secuencia de Fibonacci de los primeros 20:\n")
for numero in secuencia_fibonacci():
    if numero % 2 != 0:
        print(numero)



    
  
    