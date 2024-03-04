# Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan fácil como podrías pensar, ya que tendremos algunos requisitos específicos.

# Léelos con atención, ya que la clase sobre la que escribes se utilizará para lanzar cohetes en misiones internacionales a Marte. Es una gran responsabilidad. ¡Contamos contigo!

# Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

# Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

# La clase en sí debería proporcionar las siguientes facilidades:

# Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
# La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second(), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.
# Emplea las siguientes sugerencias:

# Todas las propiedades del objeto deben ser privadas.
# Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.

               #este es el borrador de la desquicia
def fun(list):
    strlis = []
    for i in list:
        if i < 10:
            i = str(i)
            i = ("0" + i)
            strlis.append(i)
        else:
            i = str(i)
            strlis.append(i)
   
    print(":".join(strlis))

class Timer:
    __hora = []
    def __init__(self, hh= 00, mm = 00, ss= 00 ):
        self.hh = hh      #estos son los atrivutos para hora, minutos y segundo
        self.mm = mm
        self.ss = ss
        self.__hora.append(hh)   #agrego los atributos a la variable de clase que es una lista
        self.__hora.append(mm)
        self.__hora.append(ss)
        #print("aca imprimo la primer hora")
        #print(self.__hora)   #muestro la variable de clase
        #print("ya la imprimi")
        fun(self.__hora)
    
    
    def next_second(self): #aca hago el metodo del siguiente segundo, funciona
        #print("segundo posterior")
        self.__newhora = []
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            
            if self.mm == 60:
                self.mm = 0
                self.hh += 1

                if self.hh == 24:
                    self.hh = 0
                    self.ss = 0
                    
        self.__newhora.append(self.hh)
        self.__newhora.append(self.mm) 
        self.__newhora.append(self.ss)  
        fun(self.__newhora)

               
                    
        #print(self.__newhora)
        

    def prev_second(self):  #acá hago el método del segundo previo, a revisarrrrrrrrrrrrrrrrrrrr
        #print("segundo previo")
        self.__prehora = []
        if self.ss == 0:
            self.ss = 59
            self.mm -= 1
        else:
            self.ss -= 1    
        
            
        if self.mm <= 0:
            self.mm = 59
        else:
            self.mm -= 1    
        

        if self.hh <= 0:
            self.hh = 23
            self.ss = 59
        else:
            self.hh -= 1   

        self.__prehora.append(self.hh)
        self.__prehora.append(self.mm)
        self.__prehora.append(self.ss)
        
        fun(self.__prehora)
        #print(self.__prehora)
        #print("chau froyyy")
        
        

obj = Timer(23 , 59 ,59)
#print(Timer)
obj.next_second()
#print(Timer)
obj.prev_second()
#print(Timer)
 
# -----------------------
# listo changuito ya anda
# -----------------------