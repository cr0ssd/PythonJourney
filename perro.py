"""perro = ["Freddie", 13, True, 8, 2010]
nombre, edad, vacunado, peso, nacimiento = perro
perro.append: (["comer", "frisbee"])
print("Mi perro se llama ", nombre, " y sus hobbies son ", perro[-1])"""

"""test = [{"Arizona": "Phoenix", "California": "Sacramento", "Hawaii":"Honolulu"}],
1000,
2000,
3000,
["hat", "t-shirt", "jeans", {"socks 1":"red", "socks2": "blue"}]

print(test[2])
print(test[0])
print(test[0]["Arizona"])
print(test[4][2])"""

"""precio = [50, 75, 46, 22, 80, 65, 8]
precio.sort()
print(precio[0])"""

"""asignaturas = ["matemáticas", "toma de decisiones", "física"]
print("Yo estudio ", asignaturas)"""

"""salario = 100000
liminferior = 8629.21
impuesto = .16

cuota_sat = 692.96
imss = 537

resta_1=(salario-liminferior)*impuesto
resta_final = resta_1+cuota+imss
result = salario - resta_final

print(result)"""


import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
mu = 0.1  # Tasa de crecimiento de la levadura
Y = 0.5   # Rendimiento de la levadura en la producción de alcohol
P0 = 1.0  # Población inicial de levadura
A0 = 0.0  # Concentración inicial de alcohol

# Tiempo de simulación
t_max = 10.0  # Tiempo máximo de simulación
dt = 0.01     # Paso de tiempo

# Inicialización de listas para almacenar resultados
t_values = [0]
P_values = [P0]
A_values = [A0]

# Simulación con el método de Euler
t = 0
P = P0
A = A0

while t < t_max:
    dP = mu * P
    dA = Y * mu * P
    
    P += dP * dt
    A += dA * dt
    t += dt
    
    t_values.append(t)
    P_values.append(P)
    A_values.append(A)

# Visualización de resultados
plt.figure(figsize=(10, 6))
plt.plot(t_values, P_values, label='Población de levadura')
plt.plot(t_values, A_values, label='Concentración de alcohol')
plt.xlabel('Tiempo')
plt.ylabel('Población / Concentración')
plt.legend()
plt.title('Simulación de fermentación de vino')
plt.grid(True)
plt.show()
