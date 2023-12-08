x = int (input())
y = int (input())
z = int (input())

if (x > 0 and y > 0 and z > 0) and (x + y > z) and (x + z > y) and (y + z > x):
    #Determinar qué tipo de triángulo es
    if x == y and x == z:
        print ("Triángulo equilátero")
    elif x != y and x != z and y != z:
        print("Triángulo escaleno")
    else:
        print("Triángulo isóceles")
else:
    print("Esto no es un triángulo")
    
