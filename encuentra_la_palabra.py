# Vamos a jugar un juego. Te daremos dos cadenas: una es una palabra (por ejemplo, "dog") y la segunda es una combinación de un grupo de caracteres.

# Tu tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?

# Por ejemplo:

# Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si;
# Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", o "g" ni en ese orden)
# Pistas:

# Debes usar las variantes de dos argumentos de las funciones pos() dentro de tu código.
# No te preocupes por mayúsculas y minúsculas.

#////datos de prueba////
# donor
# Nabucodonosor     si

# donut
# Nabucodonosor     no

cadena = "Nabucodonosor"

palabra1 = "donor"
palabra2 = "donut"

mipalabra = input("por favor ingresa una palabra: ")
cadena.lower()
mipalabra.lower() 
encontradas = ''
for ch in mipalabra:
    if ch in cadena:
        encontradas += ch
print(encontradas)
if encontradas == mipalabra:
    print("Se encontró tu palabra") 
else:
    print("No encontramos tu palabra")           