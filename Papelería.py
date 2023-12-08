num_articulos_comprados = 0
total_a_pagar = 0

quiereotracosa = input("¿Desea comprar un artículo? (S/N): ")

while quiereotracosa == "S" or quiereotracosa == "s":
    precio = float(input("Precio del artículo: "))
    cantidad = int(input("Cantidad a comprar: "))
    costo_actual = precio * cantidad
    num_articulos_comprados += 1
    total_a_pagar += costo_actual
    
    quiereotracosa = input("¿Desea comprar otro artículo? (S/N): ")

print("Número de artículos comprados =", num_articulos_comprados)
print("Total a pagar =", total_a_pagar)