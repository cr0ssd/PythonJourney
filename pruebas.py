numero = int(input("De qué numero quieres saber la tabla? "))

print("Tabla de multiplicar del", numero, ":")

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
