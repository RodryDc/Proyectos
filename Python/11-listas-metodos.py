lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

lenguajes.insert(3, "Go") #inserta Go en la posicion 3
print(lenguajes)

lenguajes.insert(0, "C") #inserta C en la posicion 0
print(lenguajes)

lenguajes.remove("Ruby") #remueve Ruby
print(lenguajes)

print("PHP" in lenguajes) #devuelve true o false si la encuentra

print(len(lenguajes)) #devuelve la longitud de la lista

lenguajes.clear() #remueve todos los elementos
print(lenguajes)