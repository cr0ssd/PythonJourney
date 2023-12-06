import math

def calcular_area_esfera(radio):
    area = 4 * math.pi * math.pow(radio, 2)
    return area

def calcular_volumen_esfera(radio):
    volumen = (4 * math.pi * math.pow(radio, 3)) / 3
    return volumen

radio = float(input("Radio: "))

area = calcular_area_esfera(radio)
volumen = calcular_volumen_esfera(radio)

result_area = round(area)
result_volumen = round (volumen)

print(f"Volumen: {result_volumen}")
print(f"Area: {result_area}")