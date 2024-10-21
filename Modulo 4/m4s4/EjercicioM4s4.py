"""EJERCICIOS:
Realice los pasos que se detallan a continuación:
1. La clase Libro está definida. Cree dos instancias de la clase Libro denominadas libro_1 y
libro_2. Luego, asigne atributos de instancia a estos objetos (usando la notación de
puntos) de la siguiente manera:
● libro_1:
○ autor = 'Dan Brown'
○ titulo = 'Infierno'
● libro_2:
○ autor = 'Dan Brown'
○ titulo = 'El Código Da Vinci'
○ ann_de_publicacion = 2003
2. En respuesta, imprima el valor del atributo __dict__ de libro_1 y libro_2.
3. Resultado al ejecutar:
1
2
print(libro_1.__dict__)
print(libro_2.__dict__):
Salida:
1
2
3
{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Da Vinci Code',
'year_of_publishment':"""


class Libro:
    def __init__(self, autor, titulo, ann_de_publicacion):
        self.author = autor
        self.title = titulo
        self.year_of_publishment = ann_de_publicacion

    def __str__(self):
        return f"1\n2\n{self.__dict__}" 

libro_1 = Libro("Dan Brown", "Infierno", 2003)
libro_2 = Libro("Dan Brown", "The Da Vinci Code", 2003)

print(libro_1.__dict__)
print(libro_2.__dict__)