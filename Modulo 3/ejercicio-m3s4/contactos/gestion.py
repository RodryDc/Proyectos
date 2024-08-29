(""")Crea un módulo llamado gestion.py dentro de una carpeta llamada
contactos .
En este módulo, define una lista llamada lista_contactos que contenga
tuplas con el nombre y email de los contactos. Inicia esta lista con
algunos contactos predefinidos.
Implementa una función agregar_contacto(nombre, email) que agregue un
nuevo contacto a lista_contactos .(""")

lista_contactos = [
    ("Juan Pérez", "juan.perez@example.com"), ("María López", "maria.lopez@example.com")]

def agregar_contacto(nombre, email):
    lista_contactos.append((nombre, email))