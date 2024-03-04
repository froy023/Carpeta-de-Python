#creo la lista con los número que quiere ver el usuario
#este es el que mejor funciona, anda con listo pero no con lista, ¿por qué???
#ESTE FROY! CONTINUA DESDE ACA...

lista = []
numerousuario = input("ingresa el número que quieras ver en el panel o preciones 'h' para salir: ")
while numerousuario != "h":
    lista.append(numerousuario)
    numerousuario = input("ingresa el número que quieras ver en el panel o preciones 'h' para salir: ")
if numerousuario == "h":
    print(lista)
#imprimo la lista para asegurarme de que se guardó en la memoria    

listo = [6,7]
#creo el diccionario con los patrones de cada número
patron = {0 : " ###\n # #\n # #\n # #\n ###\n\n", 1 :"  #\n  #\n  #\n  #\n  #\n\n", 2: "###\n  #\n###\n#  \n###\n\n" ,3 : " ###\n   #\n ###\n   #\n ###\n\n",4 : " # #\n # #\n ###\n   #\n   #\n\n",5 : " ###\n #  \n ###\n   #\n ###\n\n",6 : " ###\n #  \n ###\n # #\n ###\n\n",7 : "###\n  #\n  #\n  #\n  #\n\n",8 : " ###\n # #\n ###\n # #\n ###\n\n",9 : " ###\n # #\n ###\n   #\n   #\n\n"}

#creo la función que itera la lista con el diccionario
def fun(a , b= patron):
    for h in patron.keys():
        if h in listo:
            print(patron[h])

#llamo la función
fun(listo)      

#imprimo un patrón para asegurarme que el código llega hasta el final
print(patron[9])

#al momento de llamar la función no lee la lista, ¿por qué pasa esto?