"""Isaac Martínez Trujillo A01735069"""
"""Sofía Montes Salazar A01735063"""

edad = int(input("Escribe tu edad: "))

if edad < 5:
    print("Entrada Gratis.")
elif 15 > edad >= 5:
    print("$250")
else:
    print("$350")