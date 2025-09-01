class Animal: 
    species = 'mamífero'
    def __init__(self , weight: float , height):   #constructor (init), self hace referencia a si mismo.
        '''
        Class animal
        weight in kg
        height in cm
        '''                 #docstring, ayuda entre programadores
        self._weight = weight       #atributos, si quiero que sea oculto se usa __
        self.height = height
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self):
        raise AttributeError('No podés cambiar el peso del animal')
    
    def speak(self):
        ...
class Dog(Animal):
    def speak(self):
        print('Guau')                     #Herencia
class Cat(Animal):
    def speak(self):
        print('Miau')
class Rat(Animal):
    def speak(self):
        print('Squick')

if __name__ == '__main__': #iniciador del bloque de código 
    animal = Animal(25,100)
    animales = [Dog{15,40}, Cat{4,20}, Rat{0.2,10}]
for a in animales:
    a.speak()


#Instancia
#Por convención las clases se definen con su primera letra en mayúscula
# el __ asgina el valor a otra variable y no sobreescribe la clase original
# dir: lista todos los métodos y atributos de un objeto 
# metodos son las funciones y los parametros son los valores 
