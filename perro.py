#Clase Perro: Crea una clase Perro que tenga atributos para el nombre, la raza y la edad del perro.
#  Añade un método que haga que el perro ladre cuando se le llame.

class perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def datos(self):
        print("nombre:",self.nombre, "raza:",self.raza, "eda:",self.edad)

    def llamar(self):
        print("haz llamado a",self.nombre)
        print("wou wou")

mi_perro= perro("mia", "labrador", "6 meses")
mi_perro.datos()
mi_perro.llamar()