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

sudoku1 = {0 :"295743861", 
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
           2 :"876192543",
           3 :"387459216",
           4 :"612387495",
           5 :"549216738",
           6 :"763524189",
           7 :"928671354",
           8 :"254938671"}
# numeros = [["#" for i in sudoku1]for h in range(9)]
# temp = [[0.0 for h in range(24)]for d in range(31)]
#print(temp)
buscar = "1","2","3","4","5","6","7","8","9"
encontrados = 0
for i in sudoku1.keys():
    for f in buscar:
            if f in sudoku1[i]:
                encontrados +=1    
        
print(encontrados)             
if encontrados == 81:
    print("""
    -------------      
    SUDOKU VÁLIDO
    -------------      
    """)
else:
    print("""
    ---------------      
    SUDOKU INVÁLIDO
    ---------------      
    """)                           



