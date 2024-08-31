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