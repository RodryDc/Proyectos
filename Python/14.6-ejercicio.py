def no_space(texto): #Elimina los espacios
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto): #Revierte el texto
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo(texto): #Funcion para saber si es palindromo  
        texto = no_space(texto)
        texto_al_reves = reverse(texto)
        return texto.lower() == texto_al_reves.lower()
        

print("oso",es_palindromo("oso"))
print("abba",es_palindromo("reconocer"))
print("amo la paloma",es_palindromo("amo la paloma"))
print("Hola mundo",es_palindromo("Hola mundo"))