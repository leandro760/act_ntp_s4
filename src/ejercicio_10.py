# Ejercicio 10: Suma de Tuplas
# Desarrolla una función que reciba dos tuplas de igual longitud y use un ciclo for para crear una nueva tupla 
# con la suma de elementos correspondientes. Ejemplo: (1,2,3) + (4,5,6) = (5,7,9).

def suma_tuplas(tupla):
    if len(tupla) != 2 or len(tupla[0]) != len(tupla[1]):
        raise ValueError("Las tuplas deben ser de igual longitud.")
    
    resultado = []
    for i in range(len(tupla[0])):
        resultado.append(tupla[0][i] + tupla[1][i])
    
    return tuple(resultado)

tupla1 = (4, 5, 6, 7)
tupla2 = (8, 9, 10, 11)

print("Suma de tuplas:", suma_tuplas((tupla1, tupla2)))
  