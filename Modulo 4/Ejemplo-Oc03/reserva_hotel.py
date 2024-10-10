class ReservaHotel:
    def __init__(self, nro_reserva, huesped, habitacion, fecha, cantidad_noches):
        self.nro_reserva = nro_reserva
        self.__huesped = huesped
        self.__habitacion = habitacion # encapsulamiento privado de la variable habitación
        self.fecha = fecha
        self.cantidad_noches = cantidad_noches
#GETTERS
    def get_habitacion(self):
        
        return self.__habitacion

    def get_huesped(self):
        return self.huesped

#SETTERS
    def set_habitacion(self, habitacion):
        if habitacion >= 1 and habitacion <= 30:
            self.__habitacion = habitacion
        else:
            print('La habitación no existe')

    def set_huesped(self, huesped):
        self.huesped = huesped


#     def crear_reserva(self):
#         print(self.huesped)
    

#     def mostrar_huesped(self):
#         print(self.huesped)

# reserva1 = ReservaHotel(1, 'Juan', 'Habitación 1', '2022-01-01', 3)
# reserva1.crear_reserva()
# reserva1.mostrar_huesped()

# reserva2 = ReservaHotel(2, 'Pedro', 'Habitación 2', '2022-01-02', 2)

# print(reserva1.get_habitacion())
# reserva1.set_habitacion(30)
# print(reserva1.get_habitacion())

# class Cliente:
#     def __init__(self,nombre, correo):
#         self.nombre = nombre
#         self.correo = correo

reserva2 = ReservaHotel(2, 'Pedro', 20, '2022-01-02', 2)
print(reserva2.get_habitacion())
nueva_habitacion = int(input("Ingrese el nuevo número de habitación: "))
reserva2.set_habitacion(nueva_habitacion)
print(reserva2.get_habitacion())