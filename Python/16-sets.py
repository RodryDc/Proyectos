#SET = significa conjunto o grupo 
#SET REMUEVE LOS DUPLICADOS

primer = {1, 1, 2, 2, 3, 4}
print(primer)
# primer.add(5) #agrega un elemento
# primer.remove(2) #remueve un elemento
# print(primer)

segundo =[3,4,5]
segundo =set(segundo) #convierte una lista en un set
print(segundo)

print("Union",primer | segundo) #union
print("Interseccion",primer & segundo) #interseccion
print("Diferencia",primer - segundo) #diferencia
print("Diferencia simetrica",primer ^ segundo) #diferencia simetrica

if 5 in segundo:
    print("5 esta en el set")