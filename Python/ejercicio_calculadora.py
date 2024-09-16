print("Bienvenido a la calculadora \npara salir escribe Salir \nLas operaciones sn suma, multi, div y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingresa el numero: ")
        if resultado.lower() == "salir":
            break
        resultado =int(resultado)
    operacion = input("Ingresa la operacion: ")
    if operacion.lower() == "salir":
        break
    numero2 = input("Ingresa el segundo numero: ")
    if numero2.lower() == "salir":
        break
    numero2 = int(numero2)
    if operacion.lower() == "suma":
        resultado += numero2
    elif operacion == "resta":
        resultado -= numero2
    elif operacion == "multi":
        resultado *= numero2
    elif operacion == "div":
        resultado /= numero2
    else:
        print("Operacion no valida")
        break

    print(f"EL resultado es {resultado}")
