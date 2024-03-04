class Timer:
    __hora = []
    def __init__(self, hh= 00, mm = 00, ss= 00 ):
        
        self.ss = ss
        self.ss = mm
        self.ss = hh
        self.__hora.append(hh)
        self.__hora.append(mm)
        self.__hora.append(ss)
        print(self.__hora)
        

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

    def next_second(self):    #acá además de pasar al siguiente segundo volvemos a hacerlo string pero dentro del mismo método
        self.__newhorastr = " "
        if self.ss == "59":
            self.ss = int(self.ss) 
            self.ss = 0
            
        else:
            self.mm = (int(self.mm) + 1)

        if self.ss < 10:
            self.ss = "0" + str(self.ss)
        else:
            self.ss = str(self.ss)    

        if self.mm == "59":
            self.mm = int(self.mm) 
            self.mm = 0
            
        else:
            self.mm = (int(self.mm) + 1)
        if self.mm < 10:
            self.mm = "0" + str(self.mm)
        else:
            self.mm = str(self.mm)
            
        if self.hh == "59":
            self.hh = int(self.hh) 
            self.hh = 0
            
        else:
            self.hh = (int(self.hh) + 1)
        if self.hh < 10:       
            self.hh = "0" + str(self.hh)
        else:
            self.hh = str(self.hh)

        self.__newhorastr = (self.hh+ ":"+self.mm+":"+ self.ss)    
        print(self.__newhorastr)
        
        


timer = Timer(23, 59, 59)
timer.__str__()
timer.next_second()