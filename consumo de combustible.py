#escribir un par de funciones que pase de km/litros a millas /galon
# 1 milla = 1609.344 metros
# 1 galon = 3.785 litros

#pasar litros cada 100km a millas por galon
a = float(input("Ingrese el consumo de de litros cada 100 km: "))
def litros_100km_a_millas_galon(a):
    return (100 /1.609) / (a / 3.785) 
resultado_a = litros_100km_a_millas_galon(a)
print("Equivale a:",(round(resultado_a,3)),"millas por galon")

#pasar de millas por galon a litros cada 100km
b = float(input("Ingrese la cantidad de millas por galon: "))
def millas_galon_a_litros_100km(b):
    return (3.785 / (19 * 1.609) * 100)
resultado_b = millas_galon_a_litros_100km(b)  
print("Equivale a :", (round(resultado_b,3),"kilometros cada 100 litros")) 