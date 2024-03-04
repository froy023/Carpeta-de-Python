# Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9. El jugador tiene que llenar el tablero de una manera muy específica:

# Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
# Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
# Cada uno de los 9 subcuadros de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.
# Si necesitas más detalles, puedes encontrarlos aquí.

# Tu tarea es escribir un programa que:

# Lea las 9 filas del Sudoku, cada una con 9 dígitos (verifica cuidadosamente si los datos ingresados son válidos).
# Da como salida Si si el Sudoku es válido y No de lo contrario.
#//////datos de pruebas///
# sudoku1          si          
# sudoku2          no

sudoku1 = {0 :"295743861", #armo los sudukos como diccionarios
           1 :"431865927", 
           2 :"876192543", 
           3 :"387459216", 
           4 :"612387495", 
           5 :"549216738",
           6 :"763524189",
           7 :"928671354",
           8 :"154938672"}
sudoku2 = {0 :"195743862",
           1 :"431865927",
           2 :"846192543",
           3 :"387459216",
           4 :"612387425",
           5 :"549216738",
           6 :"763524189",
           7 :"924671354",
           8 :"254932671"}
# numeros = [["#" for i in sudoku1]for h in range(9)]
# temp = [[0.0 for h in range(24)]for d in range(31)]
#print(temp)
buscar = "1","2","3","4","5","6","7","8","9" #armo una variable con todos los números str a buscar
 
encontrados = 0 #contador de coincidencias 
for i in sudoku1.keys():  #itero a través de las claves
    for f in buscar:  #si la variable a buscar...
            if f in sudoku1[i]: #también se encuentra aquí
                encontrados +=1    #sumo 1 al contador
        
print(encontrados)             
if encontrados == 81:  #tiene que haber 81 casualidades
    print("""
    -------------      
    SUDOKU N°1 VÁLIDO
    -------------      
    """)
else:           # de lo contrario no se válido el sudoku
    print("""
    ---------------      
    SUDOKU N°1 INVÁLIDO
    ---------------      
    """)                           

rastreados = 0  #hago todo lo mismo con el segundo sudoku
for i in sudoku2.keys():
    for f in buscar:
            if f in sudoku2[i]:
                rastreados +=1    
        
print(rastreados)             
if rastreados == 81:
    print("""
    -------------      
    SUDOKU N°2 VÁLIDO
    -------------      
    """)
else:
    print("""
    ---------------      
    SUDOKU N°2 INVÁLIDO
    ---------------      
    """)                           


