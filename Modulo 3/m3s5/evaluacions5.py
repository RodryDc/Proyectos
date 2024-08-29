(""")Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
consonantes restantes y su posición dentro de dicha palabra.(""")
 

palabra = "paralelepípedo"
vocales = "aeiouáéíóú"

print("Palabra:", palabra)

for i in range(len(palabra)):
    letra = palabra[i]
    if letra.lower() not in vocales:
        print("Consonante:", letra, "Posición:", i)

    


