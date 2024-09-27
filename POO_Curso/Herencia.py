class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def mentar(self):
        print(f"{self.nombre} te la está mentando")

class artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

#Asi se heredan las instancias de la clase padre
class empleado(persona): 
   def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
       super().__init__(self,nombre, edad, nacionalidad)
       self.trabajo=trabajo
       self.salario=salario

#Herencia multiple
class empleadoartista(persona,artista): #Definimos el nombre de la clase y las otras clases que contienen los atributos a heredar
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        persona.__init__(self,nombre,edad,nacionalidad)#Decimos de que clase y que parametros deseamos heredar
        artista.__init__(self,habilidad)
        self.salario=salario #Se agregan las que son propias de esta clase (nuevos atributos)
        self.empresa=empresa
    def presentarse(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} , yo {self.habilidad} , me pagan {self.salario} y trabajo en {self.empresa}")

pablo=empleadoartista("Pablo","24 años","0","Canto","300000","google")
pablo.presentarse()


