#Clase de un banco: Crea una clase llamada Banco con atributos como nombre, ubicacion y cuentas.
#  Las cuentas deben ser una lista de diccionarios, donde cada diccionario representa una cuenta con claves como numero_de_cuenta y saldo.
#  Crea métodos para agregar cuentas, depositar y retirar dinero.

class banco:

    def __init__(self, nombre, ubicacion):
        self.ubicacion = ubicacion
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, numero_de_cuenta, saldo):
        self.cuentas.append({"numero_de_cuenta": numero_de_cuenta, "saldo": saldo})


    def mostrar_Saldo(self):
            for cuenta in self.cuentas:
                if cuenta["numero_de_cuenta"] == numero_de_cuenta:
                    print(cuenta["saldo"])
            return "Cuenta no encontrada"

    def depositar(self, numero_de_cuenta, cantidad):
        for cuenta in self.cuentas:
            if cuenta["numero_de_cuenta"] == numero_de_cuenta:
                cuenta["saldo"] += cantidad
                return "Depósito exitoso"
        return "Cuenta no encontrada"

    def retirar(self, numero_de_cuenta, cantidad):
        for cuenta in self.cuentas:
            if cuenta["numero_de_cuenta"] == numero_de_cuenta:
                if cuenta["saldo"] >= cantidad:
                    cuenta["saldo"] -= cantidad
                    return "Retiro exitoso"
                else:
                    return "Saldo insuficiente"
        return "Cuenta no encontrada"

mi_banco = banco("Banco tura", "Colombia")

while True:
    print("1. Agregar cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    print("5 mostrar saldo")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero_de_cuenta = input("Ingresa el número de cuenta: ")
        saldo = float(input("Ingresa el saldo inicial: "))
        mi_banco.agregar_cuenta(numero_de_cuenta, saldo)
    elif opcion == "2":
        numero_de_cuenta = input("Ingresa el número de cuenta: ")
        cantidad = float(input("Ingresa la cantidad a depositar: "))
        print(mi_banco.depositar(numero_de_cuenta, cantidad))
    elif opcion == "3":
        numero_de_cuenta = input("Ingresa el número de cuenta: ")
        cantidad = float(input("Ingresa la cantidad a retirar: "))
        print(mi_banco.retirar(numero_de_cuenta, cantidad))

    elif opcion == "4":
        numero_de_cuenta = input("Ingresa el número de cuenta: ")
        mi_banco.mostrar_Saldo()

    elif opcion == "5":
        break




