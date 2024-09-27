#Getters
class pelicula:
    def __init__(self,title,rating):
        self._title=title
        self.rating=rating

    def get_title(self):  #Aqui esta el getter , con el formato de escritura
        return self._title
    
print("TRabajdno con getters")
mi_pelicula=pelicula("El padrino",5.0)
print(mi_pelicula.get_title())  #Aqui obtenermos el valor de la variable usando getter

print('------------------------------------------------------')
#Setters
class perro:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self.edad=edad
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nuevo_nombre):  #Aqui agregmaos un nuevo nombre a la variable
        if isinstance(nuevo_nombre,str) and nuevo_nombre.isalpha():
            self._nombre=nuevo_nombre
        else:
            print("Ingresa un valor valido")

print("TRabajdno con Setters")
mi_perro=perro("juancho",3)

print(mi_perro.get_nombre())

#Settear un nuevo nombre e imprimir en pantalla
mi_perro.set_nombre("Lalo")
print("El nuevo nombre es:",mi_perro.get_nombre())