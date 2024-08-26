(""")Dada la siguiente lista de nombres:
•Harry Houdini
•Newton
•David Blaine
•Hawking
•Messi
•Teller
•Einstein
•Pele
•Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.(""")

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"] #Lista de nombres

magos = ["Harry Houdini", "David Blaine", "Teller"] #Lista de magos

cientificos = ["Newton", "Hawking", "Einstein"] #Lista de científicos

otros = ["Messi", "Pele", "Juanes"] #Lista de otros

def hacer_grandioso(): #Función para hacer grandioso a los magos
    i=0
    while i < (len(magos)):        
        magos[i] = "El gran " + magos[i]
        i += 1
    

def imprimir_nombres(personajes): #Función para imprimir nombres
    for personaje in personajes:
        print(personaje)

print("\nNombres antes de ser modificados:")
imprimir_nombres(nombres)  #Imprimir nombres

print("\nNombres de los magos grandiosos:")
hacer_grandioso() #Hacer grandioso
imprimir_nombres(magos) #Imprimir magos

print("\nNombres de los científicos:")
imprimir_nombres(cientificos) #Imprimir cientificos

print("\nNombres de los restantes:")
imprimir_nombres(otros) #Imprimir otros
