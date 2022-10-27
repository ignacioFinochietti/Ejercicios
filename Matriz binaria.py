import random

def buscarunos(mat):
    cantunos = [0] * 4
    mitad = len(mat) // 2
    for f, fila in enumerate(mat):
        if f<mitad:  # Mitad superior
            cantunos[0] = cantunos[0] + fila[:mitad].count(1)  # Primer cuadrante
            cantunos[1] = cantunos[1] + fila[mitad:].count(1)  # Segundo cuadrante
        else:        # Mitad inferior
            cantunos[2] = cantunos[2] + fila[:mitad].count(1)  # Tercer cuadrante
            cantunos[3] = cantunos[3] + fila[mitad:].count(1)  # Cuarto cuadrante
    return cantunos.index(max(cantunos)), max(cantunos)  # Devolvemos el máximo de la lista y su posición

# Generamos la matriz directamente con los números al azar usando listas por comprensión anidadas
n = int(input("Tamaño de la matriz? "))
while n<=0 or n%2!=0:
    print("El tamaño debe ser un número par positivo.")
    n = int(input("\nTamaño de la matriz? "))
matriz = [[random.randint(0, 1) for c in range(n)] for f in range(n)]
print()
for f in matriz:
    for elemento in f:
        print("%3d" %elemento, end="")
    print()
cuadrante, cant = buscarunos(matriz)
print()
print("El cuadrante con mayor cantidad de unos es el", cuadrante+1, "con", cant, "unos")
