# Escribir un programa que genere una lista con los números del 1 al 20 y muestre por pantalla, utilizando
# rango de índices, sólo los números pares.
lista = []
cadena = ''
for i in range(1 , 21):
    lista.append(i)
print(lista)
for i in lista:
    if i % 2 == 0:
        print(i)
    