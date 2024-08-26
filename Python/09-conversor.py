temperatura = float(input("Ingrese la temperatua a convertir: ")) #ingreso la temperatura
escala = input("C (Celsius) o F (Fahrenheit): ").lower() #elijo la escala

if escala == "c":
    resultado = (temperatura * 1.8) + 32
elif escala == "f":
    resultado = (temperatura - 32) * 5 / 9
else:
    print("Escala no valida")

print("La temperatura es: ", resultado)