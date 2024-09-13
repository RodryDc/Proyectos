def saludo(jornada, nombre="invitado", apellido="externo"):
    if type(nombre and jornada) == str:
        print(f"Buenas {jornada}, {nombre} {apellido}")
    else:
        print(f"El parametro {nombre} no es un string. Intenta con un texto")


# saludo("tarde")
# saludo("tarde","Carlos")
# saludo(4,"Carlos")
# saludo("noches","aedo",4)
saludo("noches",apellido="aedo")

