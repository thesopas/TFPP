import math
import random 
import os 
#se puede llamar solo la función necesaria:
#por ejem: from math import ceil

print(math.ceil(3.5))
print(math.floor(3.5))
print(math.sqrt(9))

print(random.random()) # Genera un float al azar entre cero y uno 
print(random.randint(1,100)) # Genera un entero al azar entre los números determinados en el argumento
nombre = ['nombre1', 'nombre2', 'nombre3']
print(random.choice(nombre))

if os.name == 'nt':
    os.system('cls')
else:
    os.system(clear)

print('¡Hola!')
print(os.getcwd) #Muestra el directorio donde se está trabajando 
