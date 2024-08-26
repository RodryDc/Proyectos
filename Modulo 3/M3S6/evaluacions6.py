(""")Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.(""")

a = int(input("Ingresa el primer numero: ")) #Asignamos el valor a la variable a
b = int(input("Ingresa el segundo numero: ")) #Asignamos el valor a la variable b
c = int(input("Ingresa el tercer numero: ")) #Asignamos el valor a la variable c

if (a > b and a > c): #Verificamos cual es el mayor
    if (b > c):
        print(a, b, c)
    else:
        print(a, c, b)
elif (b > a and b > c):
    if (a > c):
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if (a > b):
        print(c, a, b)
    else:
        print(c, b, a)