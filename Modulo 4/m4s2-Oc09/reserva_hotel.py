class ReservaHotel:
    
    def __init__(self,nro_reserva,huesped,habitacion,fecha,cantidad_noches):
        self.__huesped = huesped #Atributo privado
        self.nro_reserva = nro_reserva
        self.__habitacion = habitacion #Atributo privado
        self.fecha = fecha
        self.cantidad_noches = cantidad_noches


    #GETTERS o Accesores
    def get_habitacion(self):
        return self.__habitacion
    
    def get_huesped(self):
        return self.__huesped
    
    #SETTERS o Mutadores
    def set_habitacion(self,habitacion):
        if habitacion >=1 and habitacion <=30:
            self.__habitacion = habitacion
        else:
            print("Error, el número de habitación debe ser entre 1 y 30.")

    def set_huesped(self,huesped):
        self.__huesped = huesped




reserva1 = ReservaHotel(2,"Fernando",20,"05-10-2024",2) #Instanciación de clase ReservaHotel

print(reserva1.get_habitacion())

nueva_habitacion = int(input("Ingrese la nueva habitación de la reserva: "))
reserva1.set_habitacion(nueva_habitacion)

print(reserva1.get_habitacion())
