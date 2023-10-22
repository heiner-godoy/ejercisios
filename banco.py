#Clase de un banco: Crea una clase llamada Banco con atributos como nombre, ubicacion y cuentas.
#  Las cuentas deben ser una lista de diccionarios, donde cada diccionario representa una cuenta con claves como numero_de_cuenta y saldo.
#  Crea métodos para agregar cuentas, depositar y retirar dinero.


class banco:
    
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.cuentas = []

    def agregar(self, numero_de_cuenta, claves, saldo):
        self.cuentas.append({"numero_de_cuenta": numero_de_cuenta, "claves": claves, "saldo": saldo})

    def depositar(self, numero_de_cuenta, claves, cantida):
        for cuenta in self.cuentas:
            if cuenta["numero_de_cuenta"] == numero_de_cuenta and cuenta["claves"] == claves:
                cuenta["saldo"] += cantida
                return "Deposito exitoso"
        return "Cuenta no encontrada >> Revisa si tu contraseña o usuario son correctos <<"

    def retirar(self, numero_de_cuenta, claves, cantida):
        for cuenta in self.cuentas:
            if cuenta["numero_de_cuenta"] == numero_de_cuenta and cuenta["claves"] == claves:
                if cuenta["saldo"] >= cantida:
                    cuenta["saldo"] -= cantida
                    return "Retiro exitoso"
                else:
                    return "Saldo insuficiente"
        return "Cuenta no encontrada >> Revisa si tu contraseña o usuario son correctos <<"

    def mostrar(self, numero_de_cuenta, claves):
        for cuenta in self.cuentas:
            if cuenta["numero_de_cuenta"] == numero_de_cuenta and cuenta["claves"] == claves:
                print(cuenta["saldo"])
                return
        return "Cuenta no encontrada >> Revisa si tu contraseña o usuario son correctos <<"

mi_banco = banco("Bancolombia", "Colombia")

while True:
    print("1. Agregar cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Mostrar saldo")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if (opcion == "1"):
        numero_de_cuenta = int(input("Tu id sera tu numero de cuenta a crear; Ingresa tu id: "))
        claves = input("Crear clave: ")
        saldo = int(input("Ingresa el saldo inicial: "))
        mi_banco.agregar(numero_de_cuenta, claves, saldo)
        print("Registro exitoso")

    elif (opcion == "2"):
        numero_de_cuenta = int(input("Ingresa numero de cuenta: "))
        claves = input("Ingresa tu clave: ")
        cantida = int(input("Ingresa el valor a depositar: "))
        print(mi_banco.depositar(numero_de_cuenta, claves, cantida))

    elif opcion == "3":
        numero_de_cuenta = int(input("Ingresa numero de cuenta: "))
        claves = input("Ingresa tu clave: ")
        cantida = int(input("Ingresa el valor a retirar: "))
        print(mi_banco.retirar(numero_de_cuenta, claves, cantida))

    elif opcion == "4":
        numero_de_cuenta = int(input("Ingresa numero de cuenta: "))
        claves = input("Ingresa tu clave: ")
        print(mi_banco.mostrar(numero_de_cuenta, claves))

    elif opcion == "5":
        break