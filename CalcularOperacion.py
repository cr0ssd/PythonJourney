def calcular_operacion(num1, num2, clave):
    if clave == 's':
        return num1 + num2
    elif clave == 'r':
        return num1 - num2
    elif clave == 'm':
        return num1 * num2
    elif clave == 'd':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error"
    else:
        return "Clave inválida"

def main():
    valor1 = int(input())
    valor2 = int(input())
    clave = input()

    resultado = calcular_operacion(valor1, valor2, clave)

    print(resultado)

main()