import os
import random
import time

points = 0
filas = 11
columnas = 21

def generar_laberinto(filas, columnas):
    laberinto = [["#" for _ in range(columnas)] for _ in range(filas)]

    def backtrack(x, y):
        laberinto[y][x] = " "
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < columnas and 0 < ny < filas and laberinto[ny][nx] == "#":
                laberinto[y + dy][x + dx] = " "
                backtrack(nx, ny)

    backtrack(1, 1)
    return laberinto

posicion = [1, 1]
salida = [filas - 2, columnas - 2]
points = 0
start_time = None

def imprimir_laberinto(laberinto):  
    os.system("clear") 
    
    for i in range(filas):
        for j in range(columnas):
            if [i, j] == posicion:
                print("P", end=" ")  
            else:
                print(laberinto[i][j], end=" ")
        print()

def agregar_power_up(laberinto):
    power_up_x, power_up_y = random.randint(1, columnas - 2), random.randint(1, filas - 2)
    laberinto[power_up_y][power_up_x] = "O"
    return power_up_x, power_up_y

def jugar_laberinto():
    global start_time
    global points
    laberinto = generar_laberinto(filas, columnas)
    
    power_up_x, power_up_y = agregar_power_up(laberinto)

    while posicion != salida:
        imprimir_laberinto(laberinto)
        direccion = input("¿Hacia dónde quieres moverte? (W/A/S/D): ").upper()
        
        if direccion == "W" and laberinto[posicion[0] - 1][posicion[1]] != "#":
            posicion[0] -= 1
        elif direccion == "A" and laberinto[posicion[0]][posicion[1] - 1] != "#":
            posicion[1] -= 1
        elif direccion == "S" and laberinto[posicion[0] + 1][posicion[1]] != "#":
            posicion[0] += 1
        elif direccion == "D" and laberinto[posicion[0]][posicion[1] + 1] != "#":
            posicion[1] += 1
        
        if [posicion[1], posicion[0]] == [power_up_x, power_up_y]:
            points += 10
            power_up_x, power_up_y = agregar_power_up(laberinto)


        if start_time is None:
            start_time = time.time()

    imprimir_laberinto(laberinto)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"¡Felicidades! Has llegado a la salida del laberinto.")
    print(f"Puntos: {points}")
    print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    jugar_laberinto()