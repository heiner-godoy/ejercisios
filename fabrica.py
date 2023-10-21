#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
#Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

class Fabrica:
    def __init__(self, color, llantas, precio):
        self.color = color
        self.llantas = llantas
        self.precio = precio

    def mostrar(self):
        print(f"color: {self.color} / llantas: {self.llantas} / precio: {self.precio}")

class moto(Fabrica):
    def mostrar(self):
        print(f"Moto / color: {self.color} / llantas: {self.llantas} / precio: {self.precio}")

class carro(Fabrica):
    def mostrar(self):
        print(f"Carro / color: {self.color} / llantas: {self.llantas} / precio: {self.precio}")




carro1 = carro("rojo", 4, 1500.0000)

moto1 = moto("roja", 2, 2000.0000)

moto1.mostrar()
carro1.mostrar()


