#Validacion de entrada
edad =-1

while edad < 0 or edad > 120:
    edad = int(input("Ingresa tu edad: "))
    print(f"Tu edad es: {edad}")
