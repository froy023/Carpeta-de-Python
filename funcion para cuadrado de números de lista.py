#defino una funcion y le pongo como parametro una lista
def list_updater(lst):
    upd_list = [] #creo una segunda lista vacia para colocar los resultados de la funcion
    for elem in lst: #bucle de lista para calcular el cuadrado de cada número
        elem **= 2
        upd_list.append(elem) #agrego los resultados a la lista nueva
    return upd_list #devuelvo la lista nueva
 
foo = [1, 2, 3, 4, 5] #lista sobre la que trabaja el bucle (que tambien va a ser el parametro)
print(list_updater(foo)) #ejecuto todo lo anterior
 