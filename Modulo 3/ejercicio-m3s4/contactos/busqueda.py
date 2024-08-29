(""") Crea un módulo llamado busqueda.py también dentro de la carpeta
contactos .
En este módulo, implementa una función buscar_contacto(nombre) que
busque contactos en la lista lista_contactos (definida en gestion.py )
cuyo nombre coincida (o contenga) con el nombre ingresado por el
usuario. Devuelve los contactos encontrados.(""")

from contactos.gestion import lista_contactos
def buscar_contacto(nombre):
    contactos_encontrados = []
    for contacto in lista_contactos:
        if nombre in contacto[0]:
            contactos_encontrados.append(contacto)
    return contactos_encontrados