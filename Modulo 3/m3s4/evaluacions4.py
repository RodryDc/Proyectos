(""")Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista.(""")

diccionario = []

for i in range(3):
    print("\nIngrese los datos de la persona ", i+1)
    nombre = input("Ingresa tu nombre: ") #Asignamos el valor a la variable nombre
    apellido = input("Ingresa tu apellido: ") #Asignamos el valor a la variable apellido
    tel = input("Ingresa tu telefono: ") #Asignamos el valor a la variable tel

    diccionario.append({ "nombre": nombre, "apellido": apellido, "tel": tel }) #Agregamos la persona al diccionario

print("\nLista de personas:")
for persona in diccionario:
    print(persona) #Imprimimos el diccionario