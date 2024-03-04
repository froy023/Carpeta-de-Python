week = ["lunes", "martes","miercoles","jueves","viernes","sabado","domingo"] #creo una lista semana con los días
mes = [week for i in range(4)] #creo un mes con las semanas
año = [mes for i in range(12)] #creo un año con los meses
#print(año[2][3][2]) --> esto comprubea si el día es miercoles
#hasta aca esta armada la matriz del año, no esta linda pero funciona xD
#apliquemos un función
def osvaldo (a=0,s=0,d=0):
    return año[a][s][d]

nombre = osvaldo(1,2,3)
print(nombre)  
x = int(input("Ingrese un número para determinar el mes, siendo 0 enero y 11 diciembre "))
y = int(input("Ingrese un número para detirmar la semana siendo 0 la primer semana y 3 la última "))
z = int(input("Ingrese un número para determinar el día del 0 a 6"))
intento = osvaldo(x,y,z)
print(intento)