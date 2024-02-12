def CrearMatrizNumeros(n):
    matriz = []
    for i in range (n):
        renglon = []
        for j in range (n):
            renglon.append(i)
        matriz.append(renglon)
    return matriz

def MuestraMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(klen(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def main():
    numero = input()
    if numero < 2:
        print("Error")
    else:
        matrizCreada = CrearMatrizNumeros
        MuestraMatriz(matrizCreada)

main()