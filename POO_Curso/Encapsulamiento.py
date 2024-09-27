class carro:
    def __init__(self,brand,year,model):
        self.brand=brand
        self.year=year
        self._model=model #Non-public atrribute # Prevent from bugs 

minave=carro("BMW","EL mas perro","2025")
#print(minave.model)

class mochila:
    def __init__(self):
        self.__items=["agua","Kit de primeros auxilios"] #El doble guion bajo indicador de no acceder a esa variable

mi_mochila=mochila()

print(mi_mochila._mochila__items) #Con este formato podemos acceder a lo valores en esa variable