#ESTE CODIGO FUE DE PRUEBA PERO FUNCIONA, OJALDREEEEE
año = []
mes = []
semana = []
dia = "a"

for i in range(4):
    semana = [dia for i in range(7)]
    mes.append(semana)

#print(mes) 
mes[0][0] = "lunes"
mes[1][0] = "lunes"
mes[2][0] = "lunes"
mes[3][0] = "lunes"
mes[0][1] = "martes"
mes[1][1] = "martes"
mes[2][1] = "martes"
mes[3][1] = "martes"
mes[0][2] = "miercoles"
mes[1][2] = "miercoles"
mes[2][2] = "miercoles"
mes[3][2] = "miercoles"
mes[0][3] = "jueves"
mes[1][3] = "jueves"
mes[2][3] = "jueves"
mes[3][3] = "jueves"
mes[0][4] = "viernes"
mes[1][4] = "viernes"
mes[2][4] = "viernes"
mes[3][4] = "viernes"
mes[0][5] = "sabado"
mes[1][5] = "sabado"
mes[2][5] = "sabado"
mes[3][5] = "sabado"
mes[0][6] = "domingo"
mes[1][6] = "domingo"
mes[2][6] = "domingo"
mes[3][6] = "domingo"
print(mes[3][5])

año = [[m for i in range (12)] mes]