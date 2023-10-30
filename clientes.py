import random
class Compania:
    def __init__(self, name):
        self.name = name
        self.clientes = {}

    def add_cliente(self):
        nif = random.randint(0,1000)
        name = input("Ingrese nombre: ")
        ubic = input("Ingrese ubicación: ")
        phone = input("Ingrese número de teléfono: ")
        correo = input("Ingrese correo: ")
        preferente = input("¿Es preferente? (si/no): ")
        cliente = {"name": name, "phone": phone, "correo": correo, "preferente": preferente.lower() == "si"}
        self.clientes[nif] = cliente

    def mostrar_clientes(self):
        for nif, cliente in self.clientes.items():
            print( "nif:",nif, "cliente:", cliente)

    def mostrar_preferente(self):
        for nif, cliente in self.clientes.items():
            if cliente["preferente"]:
                print("NIF", nif, ":", cliente["name"])
clientes = Compania("Trululu")
while True: 
    opc =int(input())   
    if opc == 1:    
        clientes.add_cliente()
    elif opc ==2:
        clientes.mostrar_clientes()
    elif opc ==3:
        clientes.mostrar_preferente()