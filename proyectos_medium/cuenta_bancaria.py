from os import system

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cuenta, saldo):
        super().__init__(nombre, edad)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def imprimir_saldo(self):
        print(f'{self.nombre} tiene un saldo de {self.saldo}')

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f'{self.nombre} ha depositado {cantidad}. Saldo actual: {self.saldo}')
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f'{self.nombre} no tiene suficiente saldo')
        else:
            self.saldo -= cantidad
            print(f'{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}')

    def __str__(self):
        return f'{super().__str__()}, Saldo: {self.saldo}'



def crear_cliente():
    nombre = input('Ingrese el nombre del cliente: ')
    edad = int(input('Ingrese la edad del cliente: '))
    numero_cuenta = input('Ingrese el numero de cuenta: ')
    saldo = float(input('Ingrese el saldo: '))
    return Cliente(nombre, edad, numero_cuenta, saldo)   



if __name__ == "__main__":

    while True:
        system('clear')
        print('1. Crear cliente')
        print('2. Depositar')
        print('3. Retirar')
        print('4. Imprimir saldo')
        print('5. Salir')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            system('clear')
            cliente = crear_cliente()
        elif opcion == '2':
            system('clear')
            cantidad = float(input('Ingrese la cantidad a depositar: '))
            cliente.depositar(cantidad)
        elif opcion == '3':
            system('clear')
            cantidad = float(input('Ingrese la cantidad a retirar: '))
            cliente.retirar(cantidad)
        elif opcion == '4':
            system('clear')
            cliente.imprimir_saldo()
        elif opcion == '5':
            break
        else:
            print('Opcion no valida')
        input('Presione enter para continuar')