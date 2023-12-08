"""Matriz con números consecutivos"""
import random

def CrearMatrizConConsecutivos(n, m):
    caracter = "X"
    pos_x = random.randint(0, n)
    pos_y = random.randint(0, m)
    consecutivo = 1
    matriz = []
    for renglon in range (n):
        renglon = []
        for columna in range (m):
            renglon.append(consecutivo)
            consecutivo += 1
        matriz.append(renglon)
    matriz [pos_x][pos_y] = caracter
    print(matriz)

def main():
    renglones=int(input())
    columnas=int(input())
    if renglones < 2 or columnas < 2:
        print("Error")
    else:
        CrearMatrizConConsecutivos(renglones, columnas)

main()

