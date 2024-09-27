class Celular():
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

    def llamar(self):
        print(f"Estas llamando de un {self.modelo}")

    def colgar(self):
        print(f"Colgaste de un {self.modelo}")

#celular1=Celular("Samsung","S23","48MP")
#celular2=Celular("Apple","Iphone 15","96MP")
#print(celular1.camara)
#print(celular2.marca)


#celular2.llamar()
#celular1.colgar()


#Ejercicio
class estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

nombre=input("Cual es tu nombre?")
edad=input("Cual es tu edad?")
grado=input("En que grado vas?")

Estudiante=estudiante(nombre,edad,grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    Nombre: {Estudiante.nombre} \n
    Edad: {Estudiante.edad}\n
    Grado:{Estudiante.grado}\n
""")
while True:
    estudiar=input()
    if (estudiar.lower()=="estudiar"):
        Estudiante.estudiar()
