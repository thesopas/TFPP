def leer_entero(mensaje = 'Ingrese un número entero: '):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Valor invalido.')

if __name__ == '__main__': # solo ejecuta esta función cuando la función tiene asignado el valor main, esto ocurre cuando se ejecuta desde el archivo "raiz", si se lo llama desde otra instancia la función cambia de nombre.
    edad = leer_entero('Ingrese su edad: ')
    if edad < 18:
        print('Usted es menor de edad.')
    else:
        print('Usted e mayor de edad.')