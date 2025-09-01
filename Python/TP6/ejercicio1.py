# Creá una clase llamda Cuenta que tenga los siguientes atributos:
# - titular (que es una persona)
# - cantidad (puede tener decimales)
# 
# Controlar que cantidad no pueda empezar en negativo 
#
# Crear properties para:
# - titular (no puede ser modificado después de creado)
# - cantidad (sólo puede modificarse mediante depositos y retiros)
#
# Agregar métodos:
# - depositar: no tiene que poder depositar negativos
# - retirar: no puede retirar más de lo que tiene
#
# 

class Account:
    def __init__(self , account_holder: str , amount: float , alias: str):
        self._account_holder = account_holder
        if amount < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._amount = amount
        self._alias = alias  #se modificará mediante un setter
    @property
    def account_holder(self):
        return self._account_holder
    @property
    def amount(self):
        return self._amount
    
    def depositar(self, monto: float) -> None:
        if monto < 0:
            raise ValueError('El monto no puede ser negativo')
        self._amount += monto

    def retirar(self, monto: float) -> None:
        if monto > self._amount:
            raise ValueError('No puede retirar más de lo que tiene')
        self._amount -= monto
    def transferir(self , monto: float , cuenta_destino: 'Account'):
        try: 
            self.retirar(monto)
            cuenta_destino.depositar(monto)
        except ValueError as err:
            print(err)

    @property
    def alias(self):
        return self._alias
    @alias.setter
    def alias(self, nuevo_alias) -> None:
        if not nuevo_alias.replace('.','').isalpha() :
         raise ValueError('El alias solo adminte caracteres alfabéticos y puntos')

def cajero(cuenta: Account) -> None:
    opcion = input('Ingrese una opción: ')
    while True:
        print('----Menu-----')
        print('1. Consultar saldo')
        print('2. Depositar')
        print('3. Retirar')
        print('4. Transferir')
    if opcion == '5':
        bre
    elif opcion == '1': 
        print(f'Saldo actual: {cuenta.amount}')
    elif opcion == '2':
        monto = float(input('Ingrese el monto a depositar: '))
        try:
            cuenta.depositar(monto)
            print(f'Saldo después del depósito: {cuenta.amount}')
        except ValueError as err:
            print(err)      
    elif opcion == '3':
        monto = float(input('Ingrese el monto a retirar: '))
        try:
            cuenta.retirar(monto)
            print(f'Saldo después del retiro: {cuenta.amount}')
        except ValueError as err:
            print(err)

def main() -> None:
    try:
        cuenta_de_miguel = Account(account_holder='Miguel' , amount=1000 , alias='miguel.yanguez')
        cuenta_de_destino = Account(account_holder='Destinatario' , amount=500 , alias='jose.garcia')
        print(cuenta_de_miguel.account_holder)
        print(cuenta_de_miguel.amount)
        cuenta_de_miguel.depositar(50000)
        print(cuenta_de_miguel.amount)
        cuenta_de_miguel.retirar(2000)
        print(cuenta_de_miguel.amount)
        cuenta_de_miguel.transferir(1000, cuenta_de_destino)
        print(cuenta_de_miguel.amount)
        print(cuenta_de_destino.amount)
        try:
            cuenta_de_miguel.account_holder = 1000000
        except AttributeError as e:
            print('No puede modificar esta cantidad')
    except Exception as err:
        print(err)
    


if __name__ == '__main__':
    main()
