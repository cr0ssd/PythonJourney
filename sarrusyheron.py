import math

def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

area = calcular_area_triangulo(a, b, c)
resultado = (area)
print(f"El área del triángulo es: {resultado}")