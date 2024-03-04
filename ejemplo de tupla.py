meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agoslto","septiembre","octubre","noviembre","diciembre") #creo la tupla

salir = False #Creo una bandera para salir del bucle

while (not salir):
    numero = int(input("Dame un número: "))
    if (numero == 0):
        salir = True
    else:
        if (numero >=1 and numero <= len(meses)):
            print(meses[numero-1])
        else:
            print("Ingresa un número entre 1 y ",len(meses))        


