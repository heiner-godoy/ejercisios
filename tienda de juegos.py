class video_juegos:

    def __init__(self, titulo, genero, plataforma, precio):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.precio = precio

    def aplicar_descuento(self, porcentaje_descuento):
        self.descuento = (self.precio * porcentaje_descuento) / 100
        self.set_total()

    def get_descuento(self):
        return self.descuento

    def set_total(self):
        self.total = (self.precio-self.descuento)

    def get_total(self):
        return self.total

juegos = []

while True:
    print("\t:.MENU.:")
    print("opcion 1: Registro de juegos")
    print("opcion 2: Aplicar descuento")
    opcion = int(input("Ingresa la opcion que deseas realizar: "))

    if(opcion == 1):
        titulo = input("ingrese el titulo del juego: ")
        genero = input("ingrese el genero del juego: ")
        plataforma = input("ingrese la plataforma del juego: ")
        precio = float(input("ingrese el precio del juego: "))
        juegos.append(video_juegos(titulo, genero, plataforma, precio))
        print(f"Titulo: {titulo} / Genero: {genero} / Plataforma: {plataforma} / Precio: {precio}")

    elif(opcion == 2):
        indice = int(input("ingresa el indice del juego: "))
        if indice >= 0 and indice < len(juegos):
            porcentaje_descuento = int(input("Descuento% : "))
            juegos[indice].aplicar_descuento(porcentaje_descuento)
            print(f"Titulo: {juegos[indice].titulo} / Genero: {juegos[indice].genero} / Plataforma: {juegos[indice].plataforma} /Precio: {juegos[indice].precio}/ Descuento: {juegos[indice].get_descuento()} / Total: {juegos[indice].get_total()}")