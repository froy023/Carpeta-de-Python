# Tu tarea es escribir un programa el cual:

# Le pida al usuario una línea de texto para encriptar.
# Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
# Imprime el texto codificado.

# Cifrado César.
text = input("Ingresa tu mensaje: ")
try:
    rango = int(input("Ingrese un rango del 1 al 25: "))
except ValueError:
    print("Este valor es incompatible, por favor intentelo nuevamnte: ")
    rango = int(input("Ingrese un rango del 1 al 25: "))
except:
    print("El número ingresado no corresponde al rango del 1 al 25, inténtelo nuevamente: ")
    rango = int(input("Ingrese un rango del 1 al 25: "))
cipher = ''
for char in text:
    if not char.isalpha():
        continue   
    code = ord(char) + rango
    if code > ord('Z'):
        code = ord('A') + (((ord(char)+rango) - ord('z')))
    cipher += chr(code)

print(cipher)


#Cifrado César - descifrando un mensaje.
cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    code = ord(char) - rango
    if code < ord('A'):
        code = ord('z') - ((ord('A')-(ord(char)+rango)))
    text += chr(code)

print(text)