# Escriba un programa que permita crear una tupla con números y muestre por pantalla el número mayor y
# el menor.
lista1 = []
lista2 = []
mayor = 0
menor = 1000000
while True:
    numero = input('Ingresá un número para agregar a una tupla: ')
    if numero == '':
        break
    lista1.append(int(numero)) #convertir en entero
tupla = tuple(lista1)
for indice in range(len(tupla)):
    if tupla[indice] > mayor:
        mayor = tupla[indice]
    if tupla[indice] < menor:
        menor = tupla[indice]
print('El mayor elemento de la tupla es ' , mayor , ' y el menor es ' , menor)




#print(lista1)
#print(lista2)
#print(tupla_mayor)
#print(mayor)
#print(menor)
#print(menor)
