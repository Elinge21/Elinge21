#Ejercicio herencia multiple

class animal:
    def comer(self):
        print("Está comiendo")

class ave(animal):
    def volar(self):
        print("Está volando")

class mamifero(animal):
    def amamantar(self):
        print("Está amamantando")

class murcielago(mamifero,ave):
    pass

Murcielago=murcielago()
Murcielago.comer()
Murcielago.volar()
Murcielago.amamantar()
