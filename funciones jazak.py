def jazak():
    print("Sabemos si tu número es par o impar")
    a = int(input("Dime tu número.."))
    if a % 2 == 0:
        print("Tu número es: ", a, "y es par.")
    else:
        print("Tu número es: ", a, "y es impar.")
        
print(
"""
--------------------------------------
+Hola amigo, vamos a jugar un juego..+
+vamos a averiguar si es par o no..  +
--------------------------------------

""")

jazak ()
print("Adios!!")
