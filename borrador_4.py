                                          #borrador BRAULIO
class Timer:   #clase principal
    __hora = []   #variable de clase
    def __init__(self, hh= 00, mm = 00, ss= 00 ):
        self.hh = hh      #estos son los atributos para hora, minutos y segundo
        self.mm = mm
        self.ss = ss
        self.__hora.append(hh)   #agrego los atributos a la variable de clase que es una lista
        self.__hora.append(mm)
        self.__hora.append(ss)
        print(self.__hora)   #muestro la variable de clase
        

    def __str__(self):      #este método es para pasar la variable de clase a string
        print("Hlla brrauliooo")
        if self.hh < 10:       #además aca aclaro que si el atributo es menor que 10 le agrego un 0 delante 
            self.hh = "0" + str(self.hh)
        else:
            self.hh = str(self.hh)

        if self.mm < 10:
            self.mm = "0" + str(self.mm)
        else:
            self.mm = str(self.mm)

        if self.ss < 10:
            self.ss = "0" + str(self.ss)
        else:
            self.ss = str(self.ss)           
        self.__horastr = (self.hh+ ":"+self.mm+":"+ self.ss)  #aca defino la variable de instancia y agrego los atributos ya convertidos a str
        
        print(self.__horastr)    #muestro la variable de instacia
        print("chau braulio")

    # def next_second(self):
    #     self.ss = (int(self.ss) += 1)
    

time = Timer(9,8,12)  #creo el objeto con los 3 atributos
time.__str__()        #llamo al método __str__ desde el objeto            #/////////HASTA ACÁ ESTÁ BIEN//////////// 