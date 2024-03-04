#vamos a buscar el dígito de la vida
#solicita al usuario que ingrese su fecha de nacimiento DDMMYYYYY
#ve sumando los dígitos entre si hasta que sólo quede un dígito
fecha = ()
try:
    fecha = str(input("Por favor ingresa tu fecha de nacimiento con números indicando los 2 primeros números para día, los 2 segundo números para mes y los últimos 4 para año respetando este formato 'DDMMYYYY': "))
except ValueError:
    print("Los datos ingresados son incorrectos. Intentelo nuevamente")    
A = len(fecha)
if A != 8:
    print("""
    ---------------------------------------
     INGRESASTE NÚMEROS DE MÁS O DE MENOS,
        intentalo nuevamente más tarde.          
    ---------------------------------------


    """)    
    exit("\n Fin del programa\n")

lista = []    #listas vacias para hacer las autosumas
lista1 = []
lista2 = []

for i in fecha:
    i = int(i)
    lista.append(i)

#print(lista) #print de test    
suma1 = sum(lista) #sumo la primer lista
#print(suma) #print test
if suma1 > 10:
    rol = str(suma1)
    for i in rol:
        i = int(i)
        lista1.append(i)
elif suma1 < 10:
    print("""
        ----------------------------------
        TU DÍGITO DE LA VIDA ES,""" ,suma1,"""
        ----------------------------------
        buble 1
        """) 
    exit("fin del programa")       
suma2 = sum(lista1) #sumo la segunda lista
if suma2 < 10:
    print("""
    ----------------------------------
    TU DÍGITO DE LA VIDA ES,""" ,suma2,"""
    ----------------------------------
    bucle 2
            """)
elif suma2 > 9:
    rol = str(suma2)
    for i in rol:
        i = int(i)
        lista2.append(i)
        suma3 = sum(lista2) #sumo la tercer lista
        print(suma3) #print de prueba
        if suma3 < 9:
            print("""
    ----------------------------------
    TU DÍGITO DE LA VIDA ES,""" ,suma3,"""
    ----------------------------------
    bucle 3
                """)



    
    