class WeekDayError(Exception):
    
    def __init__(self, day):
        dias = ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]
        if day not in dias:
            raise WeekDayError


class Weeker:  #creo la clase

    __week = {"Lun":1, "Mar":2, "Mie":3, "Jue":4 , "Vie":5, "Sab":6, "Dom":7} #esta variable de clase tiene dic con dias y num asignados
    __week2 = {1: "Lun", 2:"Mar", 3:"Mie", 4:"Jue", 5:"Vie", 6:"Sab", 7:"Dom"}
    def __init__(self, day): 
        self.__day = day #defino q el constructor cree la variable de instancia con el atributo q se le asigna
        self.__numday = self.__week[self.__day]  #calculo q numero de dia de la semana es
        print("primera impresion")        #aca hago 3 print para probar
        print(self.__day)
        print(self.__numday)
        


    def __str__(self):  #este metodo retorna la impresion del dia q corresponde
        print("segunda impresion")
        return self.__day
    
    def add_days(self, n):  #esta método calcula q día de la semana es si nos adelantamos n cantidad de día
        self.__add = n % 7
        print("imprimo add")
        print(self.__add)
        self.__numsiguiente = self.__add + self.__numday
        print("imprimo numero siguiente")
        print(self.__numsiguiente)   #este es el número del día de la semana q corresponde froy
        self.__diasiguiente = self.__week2[self.__numsiguiente] #busco el nombre del día en el segundo diccionario
        self.__numday = self.__numsiguiente   #aca establezco el día de la semana en el nuevo número para el próximo método
        return print(self.__diasiguiente)

    def subtract_days(self, n):
        self.__sub = n % 7  #esto da 2
        if self.__numday > self.__sub:  #si el numero del día (2) es mayor que lo q hay q retroceder..
            self.__subday = self.__numday - self.__sub
        elif self.__sub > self.__numday: #si lo q hay que retroceder es mayor que el número del día...
            self.__subday = ( 7 - (self.__sub - self.__numday))
        else:
            self.__subday = 7  #si son iguales, la diferencia va a ser 0, por lo tanto es domingo
        print("print self__subday", self.__subday)
        print("print num day", self.__numday)
        self.__numday = (self.__week2[self.__subday])   #actualizo el número dia       
        return print(self.__numday)  #devuelvo la impresión del nuevo día
    


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
  