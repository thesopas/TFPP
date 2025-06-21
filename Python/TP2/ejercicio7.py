#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo 
#impositivo que le corresponde 

renta = int(input('Ingrese el valor de su renta anual: '))

if renta < 10000:
    imposicion = renta * 0.05
    print('Debe tributar ')
    print(imposicion)
elif renta >= 10000 and renta < 20000:
    imposicion = renta * 0.15
    print('Debe tributar ')
    print(imposicion)
elif renta >= 20000 and renta < 35000:
    imposicion = renta * 0.2
    print('Debe tributar ')
    print(imposicion)
elif renta >= 35000 and renta < 60000:
    imposicion = renta * 0.3
    print('Debe tributar ')
    print(imposicion)
else:
    imposicion = renta * 0.45
    print('Debe tributar ')
    print(imposicion)