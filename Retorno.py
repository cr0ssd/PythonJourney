"""Isaac Martínez Trujillo A01735069"""
"""Sofía Montes Salazar A01735063"""

inversion = float(input("Cantidad invertida: "))
interesPorcentaje = float(input("Tasa de interés en porcentaje: "))
anios = int(input("Cantidad de años que durará la inversión: "))

contadorAnios = 1
numInteres = interesPorcentaje/100
anioTasa = 0

while contadorAnios <= anios:
    contadorAnios += 1
    inversion = (numInteres * inversion)+inversion
    print(inversion)