
# Solución de Trabajo Práctico Nº 1
# Daniel Fernando Dantur
# •
# 18 ago
# TP1.2 tiene la soución al TP utilizando una función para el menú.
# TP1.3 implementa el mismo menú pero utilizando una clase cajero.

# TP1.2-Cuenta.py
# Texto

# TP1.3-Cuenta.py
# Texto
# Comentarios de la clase

# Agregar comentario para la clase…

# Creamos un cajero automático con poo

import sys
import os

class Cuenta:
    def __init__(self, titular: str, saldo: float, alias: str):
        self.__titular = titular
        if saldo < 0:
            raise ValueError('La saldo no puede ser negativa')
        self.__saldo = saldo
        self.__alias = alias

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def alias(self):
        return self.__alias
    
    @alias.setter
    def alias(self, nuevo_alias: str) -> None:
        if not nuevo_alias.replace('.', '').isalpha():
            raise ValueError('El alias solo puede contener caracteres ' \
            'alfabéticos y el signo punto')
        self.__alias = nuevo_alias.lower()
    
    def depositar(self, monto: float) -> None:
        if monto < 0:
            raise ValueError('El monto no puede ser negativo')
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        if monto > self.__saldo:
            raise ValueError('No puede retirar más de lo que tiene')
        self.__saldo -= monto

    def transferir(self, monto: float, cuenta_destino: 'Cuenta'):
        try:
            self.retirar(monto)
            cuenta_destino.depositar(monto)
        except ValueError as err:
            print(err)


class Menu:
    cuenta_activa: Cuenta | None = None  #Ayuda a la hora de escribir cuenta y detectar errores
    
    def ejecutar(cls): #Los objetos reciben los atributos de instancia 
        ...
class MenuEsperando(Menu):
    def ejecutar(cls):
        print('Bienvenido al cajero automático')
        alias = input('Ingrese el alias de su cuenta: ')
        for cuenta in CajeroAutomatico.cuentas:
            if cuenta.alias == alias:
                Menu.cuenta_activa = cuenta
                return MenuPrincipal()
        return cls()

class MenuPrincipal(Menu):
    @classmethod
    def ejecutar(cls):
        print(f'Bienvenido {Menu.cuenta_activa.titular}')
        print('1. Consultar saldo')
        print('2. Hacer un depósito')
        print('3. Retirar dinero')
        print('4. Hacer una transferencia') 
        print('5. Salir')
        opcion = input('Ingrese una opción: ')
        match opcion:
            case '1':
                return MenuSaldo()
            case '2':
                return MenuDeposito()
            case '3':
                return MenuRetiro()
            case '4':
                return MenuTransferencia()
            case '5':
                return MenuFinalizado()
            case _:
                return cls()     #Retorna al menú principal en caso de fracaso (devuelve el menú que haya llamado ejecutar)


class MenuSaldo(Menu):
    @classmethod
    def ejecutar(cls):
        print

class MenuDeposito(Menu):
    @classmethod
    def ejecutar(cls):
        ...

class MenuRetiro(Menu):
    @classmethod
    def ejecutar(cls):
        ... 

class MenuTransferencia(Menu):
    @classmethod
    def ejecutar(cls):
        ...

class MenuFinalizado(Menu):
    @classmethod
    def ejecutar(cls):
        ...
class MenuExito
        

class CajeroAutomatico:
    cuentas = [
        Cuenta(titular='Daniel Dantur', saldo=1000, alias='dani.dantur'),
        Cuenta(titular='José García', saldo=0, alias='jose.garcia'),
        Cuenta(titular='Juan Pérez', saldo=500, alias='juan.perez'),
        Cuenta(titular='María Rodríguez', saldo=2000, alias='maria.rodriguez'),
        Cuenta(titular='Pedro Gómez', saldo=3000, alias='pedro.gomez'),
        Cuenta(titular='Ana López', saldo=1500, alias='ana.lopez')
        ]
    menu: Menu = MenuEsperando()  #agregación, es una parte de CAJERO 
    @classmethod
    def mainloop(cls):
        while True:
            cls.menu = cls.menu.ejecutar() 
def main() -> None:
    try:
        CajeroAutomatico.mainloop()
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()