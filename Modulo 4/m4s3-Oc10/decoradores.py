def mi_decorador(funcion):

    def envoltorio(*args, **kwargs): #función decorada nose q parametros recibe por eso pongo *args y **kwargs
        print("esto se ejecuta antes de la función decorada")
        resultado = funcion(*args, **kwargs)
        print("esto se ejecuta después de la función decorada")
        return resultado
        
    return envoltorio

# def imprimir(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# imprimir(nombre="Juan", edad=30, ciudad="Madrid")

@mi_decorador
def suma(a, b):
    print(a + b)

calculo = suma(3, 2)