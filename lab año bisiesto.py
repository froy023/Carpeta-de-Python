#Los años bisiestos son multiplos de 4, anque no son multiplos de 100, pero si de 400

def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 ==0)

print("Comprobador de años bisiestos")

fecha = int(input("Escribe un año y te diré si es bisiesto: "))   

if es_bisiesto(fecha):
    print("El año",fecha ,"es un año bisiesto.")

else:
    print("El año" ,fecha," no es un año bisiesto.")    