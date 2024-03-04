# Tu tarea es implementar la clase Queue con dos operaciones básicas:

# put(elemento), que coloca un elemento al final de la cola.
# get(), que toma un elemento del principio de la cola y lo devuelve como resultado (la cola no puede estar vacía para realizarlo correctamente).
# Sigue las sugerencias:

# Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
# put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos del final de la lista.
# Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala cuando get() intente operar en una lista vacía.


class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.append(elem)

    def pop(self):
        val = self.__list[0]
        del self.__list[0]
        return val
        

    def get(self):
        #assert self.__list[0] == None  #acá está fallando por eso no te ejecuta el bucle try
        
        return self.__list[0]

class QueueError(Queue): 
    def __init__(self):
        Queue.__init(self)
        if self.__list == None:
            print("Algún elemento extraño entró en la pila..")

que = Queue()
que.put(1)
que.put("perro")
que.put(False)


# for i in range (3):
#     print(que.pop())

# try:
#     for i in range(4):
#         print(que.get())
#         que.pop()
# except IndexError:        
#     print("No hay más elementos en la pila")
# except LookupError:
#     print("referencia de pila no válida..")    
# except:
#     print("Queue error")

try:
    for i in range(4):
        print(que.get())
        que.pop()
except AssertionError:
    print("Lo sentimos, esta pila está vacia")
except:
    print("Queue error")            

#Ya quedó froy    