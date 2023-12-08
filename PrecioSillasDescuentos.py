def PrecioSillas(silla, cliente, cantidad):
    precios = {
        'B': 700.00,
        'E': 900.00,
        'L': 1500.00
    }
    
    PrecioNormal = precios[silla] * cantidad
    
    if cliente == 'N':
        if PrecioNormal >= 20000:
            descuento = 0.15
        elif PrecioNormal >= 10000:
            descuento = 0.10
        else:
            descuento = 0
    elif cliente == 'F':
        descuento = 0.20
    else:
        descuento = 0
    
    PrecioConDescuento = PrecioNormal * descuento
    PrecioFinal = PrecioNormal - PrecioConDescuento
    
    return PrecioNormal, PrecioConDescuento, PrecioFinal

TipoSilla = input("Tipo de silla: ")
TipoCliente = input("Tipo de cliente: ")
CuantasSillas = int(input("¿Cuántas sillas?: "))

precio, descuento, total = PrecioSillas(TipoSilla, TipoCliente, CuantasSillas)
print("Precio normal:", precio)
print("Descuento:", descuento)
print("Total con descuento:", total)