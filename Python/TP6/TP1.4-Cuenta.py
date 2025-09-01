# Creamos un cajero automático con poo

import sys
import os
import time

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
    cuenta_activa: Cuenta
    mensaje: str = ''
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        ...

class MenuEsperando(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        print('Bienvenido al cajero automático')
        alias = input('Ingrese el alias de su cuenta: ')
        for cuenta in CajeroAutomatico.cuentas:
            if cuenta.alias == alias:
                Menu.cuenta_activa = cuenta
                return MenuPrincipal
        return cls

class MenuPrincipal(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        print(f'Bienvenido {Menu.cuenta_activa.titular}')
        print('1. Consultar saldo')
        print('2. Hacer un depósito')
        print('3. Retirar dinero')
        print('4. Hacer una transferencia')
        print('5. Salir')
        opcion = input('Ingrese una opción: ')
        match opcion:
            case '1':
                return MenuSaldo
            case '2':
                return MenuDeposito
            case '3':
                return MenuRetiro
            case '4':
                return MenuTransferencia
            case '5':
                return MenuFinalizado
            case _:                
                return cls
            
class MenuSaldo(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        print(f'Saldo: ${Menu.cuenta_activa.saldo:.2f}')
        input('Presione enter para continuar')
        return MenuPrincipal

class MenuDeposito(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        try:
            monto = float(input('Ingrese el monto a depositar: '))
            Menu.cuenta_activa.depositar(monto)
            Menu.mensaje = 'Depósito realizado con éxito'
            return MenuExito
        except ValueError as err:
            Menu.mensaje = str(err)
            return MenuFinalizado

class MenuRetiro(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        try:
            monto = float(input('Ingrese el monto a retirar: '))
            Menu.cuenta_activa.retirar(monto)
            Menu.mensaje = 'Retiro realizado con éxito'
            return MenuExito
        except ValueError as err:
            Menu.mensaje = str(err)
            return MenuFinalizado

class MenuTransferencia(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        try:
            alias_cuenta_destino = input('Ingrese el alias de la cuenta destino: ')
            for cuenta_destino in CajeroAutomatico.cuentas:
                if cuenta_destino.alias == alias_cuenta_destino:
                    monto = float(input('Ingrese el monto a transferir: '))
                    Menu.cuenta_activa.transferir(monto, cuenta_destino)
                    Menu.mensaje = 'Transferencia realizada con éxito'
                    return MenuExito
            Menu.mensaje = 'Cuenta destino no encontrada'
            return MenuFinalizado
        except ValueError as err:
            Menu.mensaje = str(err)
            return MenuFinalizado

class MenuFinalizado(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        print(Menu.mensaje)
        print('Puede retirar la tarjeta.')
        time.sleep(3)
        return MenuEsperando

class MenuExito(Menu):
    @classmethod
    def ejecutar(cls) -> type['Menu']:
        print(Menu.mensaje)
        time.sleep(3)
        return MenuPrincipal

class CajeroAutomatico:
    cuentas = [
        Cuenta(titular='Daniel Dantur', saldo=1000, alias='dani.dantur'),
        Cuenta(titular='José García', saldo=0, alias='jose.garcia'),
        Cuenta(titular='Juan Pérez', saldo=500, alias='juan.perez'),
        Cuenta(titular='María Rodríguez', saldo=2000, alias='maria.rodriguez'),
        Cuenta(titular='Pedro Gómez', saldo=3000, alias='pedro.gomez'),
        Cuenta(titular='Ana López', saldo=1500, alias='ana.lopez')
    ]

    menu: type[Menu] = MenuEsperando

    @classmethod
    def mainLoop(cls):
        try:
            while True:
                if sys.platform == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

                cls.mostrar_cuentas()
                cls.menu = cls.menu.ejecutar()
        except KeyboardInterrupt:
            print('\nApagando...')

    @classmethod
    def mostrar_cuentas(cls):
        print(f'{'#' * 50}')
        for cuenta in cls.cuentas:
            print(f'{cuenta.alias}: {cuenta.titular} - ${cuenta.saldo:.2f}')
        print(f'{"#" * 50}')

def main() -> None:
    try:
       CajeroAutomatico.mainLoop()
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()