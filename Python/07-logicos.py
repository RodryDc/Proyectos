edad = 22

print(edad >= 18 and edad <= 25) #and
print(edad >= 18 or edad <= 25) #or
print(not (edad >= 18 and edad <= 25)) #not

gas=True
encendido = True

if gas and encendido:
    print("encendido")
else:
    print("apagado")

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad >= 18):
    print("puedes avanzar")

