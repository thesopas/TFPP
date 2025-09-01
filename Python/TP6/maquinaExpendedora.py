class MaquinaExpendedora:
    bebidas = {
    'Coca-Cola' : {'Precio':1500 , 'Tamaño':'500ml'},
    'Sprite' : {'Precio':2600 , 'Tamaño':'500ml'},
    'Fanta' : {'Precio':1400 , 'Tamaño':'500ml'}
}
    snacks = {
    'Lays' : {'Precio':3000 , 'Peso':'85gr'},
    'Saladix' : {'Precio' : 1100 , 'Peso' : '100gr'},
    'Tafí' : {'Precio' : 1200 , 'Peso' : '100gr'}
    }
class Menu:
    ...
class MenuPrincipal(Menu):
    try:
        monto = int(input('Ingrese dinero: '))
    except:
        raise ValueError('El monto dede ser entero')
class MenuProductos(Menu):
    try:
        monto X
class MenuBebidas(Menu):
    ...
class MenuSnacks(Menu):
    ...
class MenuFinalizar(Menu):
    ...
class MenuSalida(Menu):
