"""Isaac Martínez Trujillo A01735069"""
"""Sofía Montes Salazar A01735063"""

expresion = input("Inserta una expresión: ")
VocalA = ["A", "a"]
VocalE = ["E", "e"]
VocalI = ["I", "i"]
VocalO = ["O", "o"]
VocalU = ["U", "u"]

ContadorA = 0
ContadorE = 0
ContadorI = 0
ContadorO = 0
ContadorU = 0

for i in expresion:
    if i in VocalA:
        ContadorA += 1
    elif i in VocalE:
        ContadorE += 1
    elif i in VocalI:
        ContadorI += 1
    elif i in VocalO:
        ContadorO += 1
    elif i in VocalU:
        ContadorU += 1

print("El número de vocales 'A' es: ", ContadorA)
print("El número de vocales 'E' es: ", ContadorE)
print("El número de vocales 'I' es: ", ContadorI)
print("El número de vocales 'O' es: ", ContadorO)
print("El número de vocales 'U' es: ", ContadorU)