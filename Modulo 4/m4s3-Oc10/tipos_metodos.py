#PASO 3
def registar_calculo(func):
	def wrapper(*args,**kwargs):
		print(f"Calculando salario para {args[0].nombre}")
		return func(*args, **kwargs)
	return wrapper

#PASO 1
class Empleado():
	def __init__(self,nombre,salario):
		self.__nombre=nombre
		self.__salario=salario

	@property
	def salario(self): 
		return self.__salario
	@salario.setter
	def salario(self,valor): 
		self.__salario=valor

	@property
	def nombre(self):
		return self.__nombre
	@nombre.setter
	def nombre(self,valor):
		self.__nombre=valor
	@registar_calculo
	def SalarioAnual(self): #metodo de instancia
		return self.__salario*12

	@staticmethod
	def validar_nombre(nombre):
		return nombre.isalpha()

	@classmethod
	def desde_cadena(cls,cadena): #metodo de clase
		nombre, salario =cadena.split("-") #separamos el nombre y el salario: DIEGO-100 -> ['DIEGO', '100']
		return cls(nombre,salario)
	def __repr__(self):
		return f"Empleado(nombre={self.__nombre},salario={self.__salario})"
	

#PASO 2
class Gerente(Empleado):
	@registar_calculo
	def SalarioAnual(self):
		return self.salario * 12 * 1.1
	
	def __str__(self):
		return f"IMPRIMINENDO GERENTE"
	def __repr__(self):
		return f"Gerente(nombre={self.nombre},salario={self.salario})"

class EmpleadoRegular(Empleado):
	def __repr__(self):
		return f"Empleado Regular(nombre={self.nombre},salario={self.salario})"


print(Empleado.__subclasses__())
print(Gerente.__bases__)
print(EmpleadoRegular.__bases__)

gerente1 =Gerente("Rodrigo",200)
emp_reg1 = EmpleadoRegular("Fernando",150)

print(gerente1.SalarioAnual())
print(emp_reg1.SalarioAnual())

gerente2 = Gerente.desde_cadena("Rodrigo-200")
print(gerente2)

print(Empleado.validar_nombre("Diego3"))
print(Empleado.validar_nombre("Diego"))



