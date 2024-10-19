from datetime import datetime # Librería para trabajar con fechas


def registro_evento(evento): # Función para registrar eventos
    with open("eventos.log", "a") as log: # Abre el archivo en modo de escritura
        hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Obtiene la fecha y hora actual en el formato deseado
        log.write(f"{hora_actual} --- {evento}\n") # Escribe el evento en el archivo


registro_evento("El usuario cerro sesión")