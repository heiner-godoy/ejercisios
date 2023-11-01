import random
import os
import time

class tragamonedas:
    def __init__(self):
        self.credits = 0
        self.coins = 0
        self.ruleta = [("NARANJA", 10), ("CAMAPANA", 15), ("BAR", 50), ("MANZANA", 5), 
                ("CEREZA", 2), ("MELÓN", 20), ("SANDIA", 25), ("BAR/BAR", 100), ("77",40), ("ESTRELLAS",30)] 

    def setcoin (self, cant):
        for i in range(cant):
            self.coins += 1
        self.credits += self.coins
        print(">>>>> has insertado coins <<<<<")

    def getcoin (self):
        return self.coins

    def getcredits(self):
        return self.credits

    def log_credits(self):
        if self.credits <= 0:
            self.credits = 0
        elif self.credits > 999:
            self.credits = 999

    def apuestas(self):
        if self.credits >= 1 :
            premio = random.choice(self.ruleta)
            print("(1) Apostar\n(2) Jugar")
            print("")
            while True:
                opci = int(input("ingresar Boton: "))
                print("")
                if opci == 1:
                    self.table()
                    print("")
                    for i, (item, valor) in enumerate(self.ruleta):
                        print(f"{i+0}. {item}: {valor}")
                    indice = int(input("Ingrese nuemro del indice: "))
                    print()
                    if indice >= 0 and indice < len(self.ruleta):
                        apostar = int(input("Ingresar credits: "))
                        if apostar > self.credits:
                            print("Insuficientes credits")
                        elif apostar <=9 and self.credits >= apostar:
                            self.credits -= apostar
                            if premio == self.ruleta[indice]:
                                resultado = (apostar*premio[1])
                                self.credits +=resultado
                                print("!Winner!")
                        else:
                            print("valor invalido")
                    else:
                        print("invalido")    
                elif opci ==2:
                    break
            
            print(f">>>>> {premio[0]} <<<<<")
        else:
            print(">>>>> insert coins <<<<<")
        time.sleep(3)
        os.system('cls')
        

    def cobrar(self):
        if self.credits >=1:
            self.coins +=self.credits
            self.credits -= self.credits

    def table(self):
        print(f"        🎉 TRAGAMONEDAS 🎉          CREDITS:  {self.credits}")

maquina = tragamonedas()
while True:
    print("")
    print("(1) Insert coins")
    print("(2) Apostar o Jugar")
    if(maquina.credits >= 1):
        print("(3) Cobrar ganancias")
    print("")
    
    opc = int(input("Button --->: "))
    time.sleep(0.2)
    os.system('cls')

    if opc == 1:
        cant = int(input("cuantas monedas vas agregar: "))
        time.sleep(0.2)
        os.system('cls')
        maquina.log_credits()
        maquina.setcoin(cant)
        time.sleep(0.6)
        os.system('cls')
        print("________________________________________________________")
        maquina.table()
        print("|------___________________------__________________------|")
        
        


    elif opc == 2:
        maquina.apuestas() 
        maquina.log_credits()
        time.sleep(5)
        os.system('cls')
        print("________________________________________________________")
        maquina.table()
        print("|------___________________------__________________------|")
        
        
    
    elif opc ==3:
        maquina.cobrar()
        time.sleep(0.6)
        os.system('cls')
        print("________________________________________________________")
        maquina.table()
        print("|------___________________------__________________------|")
    else:
        print("")
        