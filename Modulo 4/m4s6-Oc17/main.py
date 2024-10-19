from formulario import Formulario

nombre = input("Ingresa tu nombre: ")
correo = input("Ingresa tu correo: ")
productos = input("Ingresa los productos que deseas: ")
nro_tarjeta = input("Ingresa el nro de tarjeta: ")
        
while True:
    try:
        
        Formulario(nombre, correo, productos, nro_tarjeta).enviar()
    except ValueError as value:
        print(value)
    except:        
        print("Ha ocurrido un error en el envio del formulario")
    else:
        print("Todo Ok")
        break
    
print("\n\n--------------------------------------------")
print("Imprimir luego del bloque try/except")

