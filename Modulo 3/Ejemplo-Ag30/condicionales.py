#Sentencia condicional
if 3>5:
    print("3 mayor que 5")
else:
    print("3 es menor que 5")

#determinamos la etapa de la vida
edad = int(input("Ingresa tu edad: "))

if edad<= 12:
    print("Esta edad corresponde a la etapa de la infancia")
elif edad <= 18:
    print("Esta edad corresponde a la etapa de la adolesencia")
elif edad <= 65:
    print("Esta edad corresponde a la etapa de la adultos")
else:
    print("Esta edad corresponde a la etapa de la vejez")



#Sentencia condicional
"""
if 3>5:
    print("3 es mayor que 5")
else:
    print("3 no es mayor que 5")
"""


#Determinar etapa de vida
"""
int() -> int   int("35") -> 35
float() -> float   float("3.14") -> 3.14
str() -> str       str(32) -> "32"

"""


"""
- Infante (hasta los 12 años)
- Adolescente (12 hasta los 18 años)
- Adulto (18 hasta 65 años)
- Adulto mayor (sobre los 65 años)
"""

"""


"""

#print("La condición es verdadera") if 5>3 else print("la condición es falsa")
'''
edad = int(input("Ingrese una edad"))

etapa = "mayor de edad" if edad>=18 else "menor de edad"

print(etapa)
'''


"""
print("Selecciona solo la inicial en mayúscula de las siguientes opciones:\n")
print("- Cesante", "Estudiante","Trabajador", "Dueño de casa", sep="\n- ")

ocupacion = input("Ingresa la ocupación según las las opciones anteriores: \n")
edad = int(input("Ingrese la edad: \n"))

mensaje_edad = "Esta edad corresponde a la de un "

if edad <= 12:

    if ocupacion == "C":
        msje = "y la persona está cesante"
    elif ocupacion == "E":
        msje = "y la persona es estudiante"
    elif ocupacion == "T":
        msje = "y la persona está trabajando"
    elif ocupacion == "D":
        msje = "y la persona es dueña de casa"
    else:
        msje = "y no se ingresó una ocupación válida"

    print(mensaje_edad + "infante", msje)

elif edad <= 12:

    if ocupacion == "C":
        msje = "y la persona está cesante"
    elif ocupacion == "E":
        msje = "y la persona es estudiante"
    elif ocupacion == "T":
        msje = "y la persona está trabajando"
    elif ocupacion == "D":
        msje = "y la persona es dueña de casa"
    else:
        msje = "y no se ingresó una ocupación válida"

    print(mensaje_edad + "adolescente", msje)
elif edad <= 65:

    if ocupacion == "C":
        msje = "y la persona está cesante"
    elif ocupacion == "E":
        msje = "y la persona es estudiante"
    elif ocupacion == "T":
        msje = "y la persona está trabajando"
    elif ocupacion == "D":
        msje = "y la persona es dueña de casa"
    else:
        msje = "y no se ingresó una ocupación válida"

    print(mensaje_edad + "Adulto", msje)
else:
    if ocupacion == "C":
        msje = "y la persona está cesante"
    elif ocupacion == "E":
        msje = "y la persona es estudiante"
    elif ocupacion == "T":
        msje = "y la persona está trabajando"
    elif ocupacion == "D":
        msje = "y la persona es dueña de casa"
    else:
        msje = "y no se ingresó una ocupación válida"

    print(mensaje_edad + "Adulto Mayor", msje)

"""

from math import trunc

edad = float(input("ingrese la edad"))

edad_entera = trunc(edad)

