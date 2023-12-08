#Año bisiesto

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def main():
    anio = int(input())
    if es_bisiesto(anio):
        print("Es bisiesto")
    else:
        print("No es bisiesto.")

main()
