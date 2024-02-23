def obtener_matriz_usuario(filas, columnas):
    matriz = []
    print("Introduce los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Elemento [{i},{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def multiplicar_matrices(X, Y):
    if len(X[0]) != len(Y):
        raise ValueError("Las matrices no se pueden multiplicar: dimensiones incompatibles")

    resultado = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                resultado[i][j] += X[i][k] * Y[k][j]

    return resultado


filas1 = int(input("Introduce el número de filas de la primera matriz: "))
columnas1 = int(input("Introduce el número de columnas de la primera matriz: "))
filas2 = int(input("Introduce el número de filas de la segunda matriz: "))
columnas2 = int(input("Introduce el número de columnas de la segunda matriz: "))

print("Introduce la matriz 1:")
matriz1 = obtener_matriz_usuario(filas1, columnas1)
print("Introduce la matriz 2:")
matriz2 = obtener_matriz_usuario(filas2, columnas2)

matriz_resultado = multiplicar_matrices(matriz1, matriz2)

print("El resultado de la multiplicación es:")
for fila in matriz_resultado:
    print(fila)
