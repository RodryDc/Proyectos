"""Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de
una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se
lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.
Ejemplo de la salida del programa:
Ingrese el salario: 5000
Traceback (most recent call last):
 File "drilling-CUE07.py", line 20, in <module>
 raise RangoSalarioError(salario)
__main__.RangoSalarioError: 5000 -> Salario no está definido en el
rango (1000 a 2000)"""

class RangoSalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
    def __str__(self):
        return f"{self.salario} -> Salario no está definido en el rango (1000 a 2000)"

salario = int(input("Ingrese el salario: "))
if (salario < 1000) or (salario > 2000):
    raise RangoSalarioError(salario)