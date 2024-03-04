# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado


def read_int(prompt, min, max):
    try:
        prompt = int(prompt)
        if prompt > min and prompt < max:
            return prompt
        else:
            print("El valor ingresado no está dentro de los límites permitidos")
            prompt = int(input("ingresa un valor entero entre -10 y 10:  "))
            if prompt > min and prompt < max:
                return prompt
            else:
                print("--->Lo sentimos pero algo salió nuevamente mal. Chequea el valor a ingresar y vuelve a ejecutar el programa.<---")
                #Hasta acá está todo bien froy
    except TypeError:
        print("TypeError1--->\n\nLo siento, al parecer ingresaste un dato no permitido.<---") 

    except ValueError:
        print("ValueError1--->\n\nLo sentimos pero el tipo el valor ingresado es incorrecto, por favor vuelve a intentarlo..<---\n\n")
        prompt = input("ingresa un valor entero entre -10 y 10:  ")
        try:
            prompt =int(prompt)
            if prompt > min and prompt < max:
                return prompt
        except:
            print("ValueError2--->\n\nLo sentimos pero algo salió nuevamente mal. Chequea el valor a ingresar y vuelve a ejecutar el programa.<---\n\n")

    except:
        print("¿¿froy que haces carajoooo, sacá la mano de ahiiiiiiiíí??")


v = read_int(prompt= input("ingresa un valor entero entre -10 y 10:  "),min = -10, max = 10)


print("""
    \n--------------
    \nEl número es:""",v,
    """\n\n--------------""")