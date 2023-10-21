#Clases y objetos: Crea una clase Auto que tenga
# atributos para el color, la marca y el modelo. 
# Añade métodos que cambien el color y muestren la información del auto.


class auto:
    
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo


    def set_color(self):
        self.color =input("Cambiar color a: ")



    def datos(self):
        print("color:",self.color, "marca:",self.marca, "modelo:",self.modelo)
mi_auto = auto("Rojo", "Toyota", "Corolla")
mi_auto.set_color()
mi_auto.datos()
