def suma(*numeros): #PARAMETROS VARIOS (ARGS)
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(f"La suma es: {resultado}") 


suma(2, 5, 7)
suma(2, 5)
suma(2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
