(""")Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
consonantes restantes y su posición dentro de dicha palabra.(""")

palabra = "paralelepipedo"

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        palabra = palabra.replace(i, "")

print(palabra)

