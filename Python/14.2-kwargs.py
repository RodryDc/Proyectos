def get_producto(**datos): #PARAMETROS NOMBRADOS (KWARGS)  
    print(datos["id"], datos["producto"])

get_producto(id=1,producto="PlayStation 5", precio=50000,stock=50)