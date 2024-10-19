# import os
# #r para leer
# #w para escribir
# #a para agregar
# #x para crear

# archivo = open("archivo1.txt","w") #abrimos el archivo si no existe lo crea
# archivo.write("Primera LInea\n") #escribimos en el archivo
# archivo.write("Segunda Linea\n") #escribimos en el archivo
# lineas = ["Linea 1\n","Linea 2\n","Linea 3\n"]
# archivo.writelines(lineas) #escribimos en el archivo las lineas del arreglo

# archivo.close() #cerramos el archivo

# archivo = open("archivo1.txt","r") #abrimos el archivo para leer

# for linea in archivo: #leemos el archivo y muestra todas las lineas
#     print(linea) #imprimimos el archivo

# print(archivo.readlines()) #leemos el archivo y muestra todas las lineas

# print(archivo.read()) #leemos el archivo y muestra tal cual esta escrito

# archivo.close() #cerramos el archivo

# archivo = open("archivo1.txt","r+") #abrimos el archivo para leer y escribir

# print(archivo.readline()) #leemos el archivo y muestra tal cual esta escrito
# archivo.write("Nueva Linea 4\n") #escribimos en el archivo
# print(archivo.read())

# archivo.close() #cerramos el archivo

# archivo = open("archivo1.txt","a") #abrimos el archivo para agregar NO SE PUEDE LEER

# archivo.write("Nueva Linea 5 en modo a\n") #escribimos en el archivo

# with open("archivo2.txt","w") as file: #abrimos el archivo para escribir y se cierra automaticamente al final 
#     for i in range(5):
#         file.write(f"Nueva Linea {i+1} de otra forma\n") #abrimos el archivo para leer

# with open("archivo3.txt","x") as file2: #abrimos el archivo para escribir
#     file2.write("Nueva Linea en modo x") #abrimos el archivo para escribir

# with open("archivo4.txt","r") as file3: #abrimos el archivo para leer
#     print(file3.read()) #abrimos el archivo para leer

# print(os.listdir()) #muestra todos los archivos
# os.remove("archivo1.txt") #eliminamos el archivo
# os.rename("archivo2.txt","archivo1.txt") #renombramos el archivo
# os.path.exists("archivo1.txt") #verifica si existe el archivo

archivo= "archivo2.txt"
with open(archivo,"w") as file: #abrimos el archivo para escribir y se cierra automaticamente al final 
    for i in range(5):
        file.write(f"Nueva Linea {i+1} de otra forma\n") #abrimos el archivo para leer