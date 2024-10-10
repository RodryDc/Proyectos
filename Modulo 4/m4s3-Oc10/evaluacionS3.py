"""EJERCICIO:
El banco posee información de sus cuentas y clientes, se identifica con su nombre, código del banco
y dirección.
Un cliente del banco puede tener una cuenta de ahorros o una cuenta corriente. Dichas cuentas
contienen la siguiente información: número de cuenta, titular y saldo. Las cuentas de ahorro guardan
información de la cantidad de retiros que se han realizado en la cuenta, y no permiten créditos.
Mientras que las cuentas corrientes permiten retiros, pero hasta un cierto límite que es propio de
cada una de ellas, e indica que el saldo es en rojo si supera el límite.
A los clientes se les conoce el nombre, dirección y número de identificación.
Las operaciones permitidas en ambas cuentas son: depósito de dinero, retiros y consulta de saldo.
El banco permite hacer transferencias de una cuenta a otra"""


class Cuenta:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def __str__(self):
        return f"CUENTA: {self._numero} TITULAR: {self._titular} SALDO: {self._saldo}"

    def depositar(self, monto):
        self._saldo += monto

    def retirar(self, monto):
        self._saldo -= monto

    def consultar(self):
        return self._saldo
    

class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self._limite = limite

    def retirar(self, monto):
        if (self._saldo + self._limite) >= monto:
            self._saldo -= monto
        else:
            print("No se puede realizar el retiro")

    def consultar(self):
        return self._saldo
    
class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
    
    def consultar(self):
        return self._saldo

    