(""")Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente(""")

def sumar(num1, num2):    
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir por cero"
    
def operaciones(num1, num2):
    suma = sumar(num1, num2)
    resta = restar(num1, num2)
    multiplicacion = multiplicar(num1, num2)
    division = dividir(num1, num2)
    return (suma, resta, multiplicacion, division)

def resultados_en_diccionario(num1, num2):
    resultados = operaciones(num1, num2)
    diccionario = {
    "Suma" : resultados[0],
    "Resta": resultados[1],
    "Multiplicacion": resultados[2],
    "Division": resultados[3]
    }
    return diccionario

num1 = int(input("Ingresa el primer numero: ")) 
num2 = int(input("Ingresa el segundo numero: ")) 
print (resultados_en_diccionario(num1,num2))
