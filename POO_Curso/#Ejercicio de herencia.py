#Ejercicio de herencia

class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def info(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} años")

class estudiante(persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    def calif(self):
        print(f"Mi grado es {self.grado}")


Pablo=persona("pablo","24")
Pablo.info()

Pablo2=estudiante("Pablo","24","8")
Pablo2.calif()