# bucles mientras

contador = 0
while contador < 10:
    print(contador, end=' ')
    contador += 1 # contador = contador + 1

# pedir al usuario números y mostrar sólo los positivos
while True:
    n = int(input('Introduce un número (0 para salir): '))
    
    if n == 0: # concidión de corte
        break  # sale del bucle
    
    if n < 0:
        continue # salta a la siguiente iteración del bucle

    print(f'El número es {n}')