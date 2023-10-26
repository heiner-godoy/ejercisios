import random
class Phone:
    def __init__(self,nif):
        self.marca = "samsung"
        self.modelo = "S23"
        self.camaraF = "24MP"
        self.camaraT = "48MP"
        self.id = id
phones = []
while True:
    opc =int(input("opc(1) fabricar  opc(2) producion: "))
    if opc == 1:
        for i in range(10):
            id = random.randint(0,10000)
            phones.append(Phone(id))
        print(">>>FABRICACION EXIOTASA")

    elif opc == 2:
        for Phone in phones:
            print(f"id: {Phone.id} Marca: {Phone.marca} Modelo: {Phone.modelo} Camara Frontal: {Phone.camaraF}, Camara Trasera: {Phone.camaraT}")

    elif opc == 3: 
        id = int(input("Ingrese el id del producto a eliminar: "))
        for phone in phones:
            if phone.id == id:
                phones.remove(phone)
                print("producto eliminado")
            else:
                print("producto no encontrado")
                








