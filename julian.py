# Usando un bucle for, generar un patrón de asteriscos que tenga un número variable de filas y columnas, 
# donde el número de filas sea igual a la longitud de una cadena de texto.
from random import randrange
aimprimir = ("el gato rogelio")
grafico = (len(aimprimir))
columnas = randrange(1,5)
#print(grafico) = 15
#print(columnas)
matriz = [["*" for h in range(len(aimprimir))]for i in range(columnas)]
print(matriz)