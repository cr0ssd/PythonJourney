def calcular_promedio():
    total = 0.0
    contador = 0
    numero = 0.0
    
    while numero >= 0:
        numero = float(input())
        
        if numero >= 0:
            total += numero
            contador += 1
    
    if contador > 0:
        promedio = total / contador
        print("El promedio de los", contador, "números es:", round(promedio, 2))
    else:
        print("Error.")

calcular_promedio()