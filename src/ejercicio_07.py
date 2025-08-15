
def estudiantes_aprobados(estudiantes):
    aprobados = ()
    for nombre, edad, promedio in estudiantes:
        estudiante = (nombre, edad, promedio)
        if promedio > 8.0:
            aprobados += (estudiante,)
    return aprobados

estudiantes = (
    ("Juan", 20, 9.5),  
    ("Ana", 22, 7.5),  
    ("Luis", 21, 8.2),  
    ("María", 23, 9.0),  
    ("Pedro", 19, 6.5)
)

print(estudiantes_aprobados(estudiantes))
    