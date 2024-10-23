"""Una de las excepciones más comunes es la división por cero. Esto puede provocar las caídas de
softwares completos, por lo que se vuelve fundamental su control; por este motivo se plantea
como uno de los controles de excepción básicos. A continuación, se dan dos variables definidas
como:
1 suma = 3000
2 contador = 0
Queremos dividir la variable suma por la variable contador.
El uso de la cláusula try... except... maneja el ZeroDivisionError. Si la división se realiza
correctamente, imprima el resultado en la consola; de lo contrario, imprima en la consola el
siguiente mensaje:
'División por cero.'"""

suma = 3000
contador = 0
try:
    print(suma / contador)
except ZeroDivisionError:
    print("División por cero.")