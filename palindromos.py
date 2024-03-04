#chequeador de palíndromos
#desarrolla un programa que solicite un mensaje usuario
#y compruebe si es o no un palíndromo

try:
    pal = str(input("Por favor ingrese su mensaje: "))
except:
    print("No se que hacer con esto..") #chequeo que el usuario ingrese lo correcto
    pal = input("Por favor ingrese su mensaje: ")   

pal = pal.upper()   
print("Tu mensaje es:", pal)
#print(pal) #print de prueba

pal2 = ("")
pal3 = []
pal4 = ("")

for ch in pal:
    if not ch.isalpha():#quito los espacios
        continue
    elif ch.isalpha():#añado las letras a la nueva lista
        pal2 += ch
#print(pal2)#print de prueba     

for i in pal2: #armo una lista invertida con cada elemento de la cadena
    pal3.insert(0, i)
pal4 = "".join(pal3)    #hago una cadena con los elementos de la lista
#print(pal3)   #print de prueba
#print(pal4)   #print de prueba

if pal.isspace():
    print("""
    ------------------------
    ESTO NO ES UN PALINDROMO
    ------------------------
    """)

    exit("\nFin del programa\n")
if pal4 == pal2:
    print("""
          
          -------------------
          Si es un palíndromo
          -------------------
          
          """)
if pal4 != pal2:
    print("""
    
    ------------------------
    Esto no es un palíndromo
    ------------------------
    
    
    """)    