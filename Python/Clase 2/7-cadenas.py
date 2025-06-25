# Cadenas como arrays

cadena = 'Programación'

print(len(cadena))  # Devuelve la longitud de la cadena

print(cadena[0])  # Devuelve el primer carácter de la cadena
print(cadena[5])  # Devuelve el sexto carácter de la cadena
print(cadena[-1])  # Devuelve el último carácter de la cadena

# for i in range(10): # Itera desde 0 hasta 9
#     print(i)  
    
for i in range(len(cadena)):
    print(cadena[i], end=' ')  # Imprime cada carácter de la cadena

for c in cadena:
    print(c, end=' ')  # Imprime cada carácter de la cadena
print()

print(cadena[0:5])  # Imprime los primeros 5 caracteres de la cadena
print(cadena[5:])  # Imprime desde el sexto carácter hasta el final
print(cadena[:5])  # Imprime desde el inicio hasta el quinto carácter
print(cadena[-5:])  # Imprime los últimos 5 caracteres de la cadena
print(cadena[0:5:2])  # Imprime los caracteres de la cadena desde el inicio hasta el quinto, saltando de 2 en 2
print(cadena[::-1])  # Imprime la cadena al revés
print(cadena[-1:0:-1]) # Invierte la cadena 

# contar cuantas letras 'a' hay en la cadena
cantidad_a = 0
for c in cadena:
    if c == 'a':
        cantidad_a += 1 # cantidad_a = cantidad_a + 1

print(cantidad_a)