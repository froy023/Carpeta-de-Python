# Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin parámetros que devuelva True si la cola está vacía y False de lo contrario.
# Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado similar al nuestro.
# A continuación, puedes copiar el código que usamos en el laboratorio anterior

class Queue:   #compruebo que la super classe funcione bien
    def __init__(self):
        self.__list = []
        
    def put(self, elem):
        self.__list.append(elem)
        return elem

    def pop(self):
        elem = self.__list[0]
        del self.__list[0]
        return elem
        

    def get(self):
        return self.__list[0]
    
class SuperQueue(Queue): #aca hago la super clase y chequeo si se hereda bien todo
    def __init__(self):
        Queue.__init__(self)
        self.__sum = 0


    def put(self, elem):
        self.__sum += 1
        return elem
        
        
    def pop(self):
        self.__sum -= 1
        return self

    def get(self):
        return self.__list[0]


    def get_sum(self):
        return self.__sum 
    #true vacia, false llena

    def check(self):
        if self.__sum == 0:
            return True
        else:
            return False
        
que = SuperQueue()
print(que.put(1))
print(que.put("perro"))            
print(que.put(False))

print(que.put(7))
que.pop()
que.pop()
que.pop()
que.pop()

if que.get_sum == 0:
    print("False Chango")
else:
    print("True MAdafacaaa!")    


print(que.check())    


#ESTA VIVOOOOOOOOOOOOOOOO!!!!!!