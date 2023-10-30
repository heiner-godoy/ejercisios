import random
class Transporte:
    def __init__(self, id, marca, modelo, color, velocidadMAX):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__pais = "colombia"
        self.velocidad = 0
        self.velocidadMAX = velocidadMAX

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, cant):
        self.velocidad += cant
        if (self.velocidad >= self.velocidadMAX):
            self.velocidad = self.velocidadMAX

    def set_frenar(self, cant):
        self.velocidad -= cant
        if (self.velocidad<0):
            self.velocidad=0

    def mostrar_vehiculo(self):
        print(f"id: {self.id} modelo: {self.modelo} marca: {self.marca} color: {self.color} origen: {self.__pais} Velocidad max: {self.velocidadMAX}")

def mostrar_vehiculos(vehiculos):
    for vehiculo in vehiculos:
        vehiculo.mostrar_vehiculo()

vehiculos = []

while True:
    opc = int(input("1. Registrar\n2. Mostrar auto\n3. Acelerar\n4. Desacelerar\n5. Mostrar todos los autos\n3. Salir\nSeleccione opcion: "))
    if opc == 1:
        n = int(input("cuantos vehiculos desea registrar: "))
        for i in range(n):
            id = random.randint(0,1000)
            marca = input(f"marca del vehiculo {i+1}: ")
            modelo = input(f"modelo del vehiculo {i+1}: ")
            color = input(f"color del vehiculo {i+1}: ")
            velocidadMAX = int(input(" ingrese id del vehiculo: "))
            print(f"Registro exitoso, id del vehiculo {i+1}: {id}  ")
            vehiculos.append(Transporte(id, marca, modelo, color, velocidadMAX))

    elif opc == 2:
        id = int(input(" ingrese id del vehiculo: "))
        for vehiculo in vehiculos:
                if vehiculo.id == id:
                    vehiculo.mostrar_vehiculo()
        else:
            print("vehiculo no encontrado")

    elif opc == 3:
        id = int(input(" ingrese id del vehiculo: "))
        for vehiculo in vehiculos:
            if vehiculo.id == id:
                cant = int(input(" cuanto deseas acelerar: "))
                vehiculo.set_velocidad(cant)
                print("vehiculo:", vehiculo.marca, "La velocidad a aumentado:", vehiculo.velocidad,"KM")
        else:
            print("vehiculo no encontrado")

    elif opc == 4:
        id = int(input(" ingrese id del vehiculo: "))
        for vehiculo in vehiculos:
            if vehiculo.id == id:
                cant = int(input(" cuanto deseas acelerar: "))
                vehiculo.set_frenar(cant)
                print("vehiculo:", vehiculo.marca, "La velocidad a disminuido:", vehiculo.velocidad,"KM")
        else:
            print("vehiculo no encontrado")

    
    elif opc == 5:
        mostrar_vehiculos(vehiculos)