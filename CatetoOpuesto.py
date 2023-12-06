import math

print ("Hipotenusa")

hipotenusa = int(input())
angulo_base = math.sin(math.radians(30))
cateto_opuesto = angulo_base * hipotenusa

resultado = round(cateto_opuesto)

print ("Cateto opuesto: " + str(resultado))