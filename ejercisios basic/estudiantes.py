class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando")
nombre =input("ingrese el nombre: ")
edad =int(input("ingrese la edad: "))
grado =input("ingrese el grado: ")

estudiante1=estudiante(nombre, edad, grado)

print(f"""DATOS DEL ESTUDIANTE:\n\n
    nombre: {estudiante1.nombre}\n
    edad: {estudiante1.edad}\n
    grado: {estudiante1.grado}\n
      """)

while True:
    estudiar=input()
    if(estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
