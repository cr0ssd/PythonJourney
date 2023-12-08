#Área y perímetro del rectángulo

def areaRect(largo, ancho):
    return largo * ancho

def perimetroRect(largo, ancho):
    return 2 * largo + 2 * ancho

def main():
    largo = float(input())
    ancho = float(input())
    opcion = input()

    if opcion == 'a':
        print(areaRect(largo, ancho))
    if opcion == 'p':
        print(perimetroRect(largo, ancho))