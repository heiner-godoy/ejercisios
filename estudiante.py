class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = {}

    def agregar_materia(self, nombre_materia, calificacion):
        self.materias[nombre_materia] = calificacion

    def cambiar_calificacion(self, nombre_materia, calificacion):
        if nombre_materia in self.materias:
            self.materias[nombre_materia] = calificacion
        else:
            print("La materia no existe.")

    def calcular_promedio(self):
        total_calificaciones = sum(self.materias.values())
        numero_materias = len(self.materias)
        return total_calificaciones / numero_materias 

# Crear una lista para almacenar a los estudiantes
estudiantes = []

while True:
    print("1. Agregar estudiante")
    print("2. Agregar materia a un estudiante")
    print("3. Cambiar calificación de un estudiante")
    print("4. Calcular promedio de un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int(input("Ingresa la edad del estudiante: "))
        grado = input("Ingresa el grado del estudiante: ")
        estudiantes.append(Estudiante(nombre, edad, grado))
    elif opcion == "2":
        nombre_estudiante = input("Ingresa el nombre del estudiante: ")
        for estudiante in estudiantes:
            if estudiante.nombre == nombre_estudiante:
                nombre_materia = input("Ingresa el nombre de la materia: ")
                calificacion = float(input("Ingresa la calificación: "))
                estudiante.agregar_materia(nombre_materia, calificacion)
                break
    elif opcion == "3":
        nombre_estudiante = input("Ingresa el nombre del estudiante: ")
        for estudiante in estudiantes:
            if estudiante.nombre == nombre_estudiante:
                nombre_materia = input("Ingresa el nombre de la materia: ")
                calificacion = float(input("Ingresa la nueva calificación: "))
                estudiante.cambiar_calificacion(nombre_materia, calificacion)
                break
    elif opcion == "4":
        nombre_estudiante = input("Ingresa el nombre del estudiante: ")
        for estudiante in estudiantes:
            if estudiante.nombre == nombre_estudiante:
                print(f"El promedio general es {estudiante.calcular_promedio()}")
                break
    elif opcion == "5":
        brea