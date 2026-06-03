notas_estudiantes = [
    [4.5, 3.8],  # Estudiante 0
    [2.0, 5.0],  # Estudiante 1
    [3.5, 4.2]   # Estudiante 2
]
j=len(notas_estudiantes)
for fila in notas_estudiantes:
    print("Notas estudiante: ",end="")
    for columna in fila:
            print(columna,end="  ")

    print()