"""Lee lista y muestra"""

def calcula_promedio(n):
    lista = []
    for actual in range(n):
        calificacion = int(input())
        lista[actual:] = [calificacion]
    suma = 0 
    for elemento in lista:
        suma += elemento
    print (lista)
    print (suma/n)

def main ():
    numero = int(input())
    while numero <= 0:
        numero = int(input("El número debe ser mayor a 0\n>>>"))
    calcula_promedio(numero)

main()
