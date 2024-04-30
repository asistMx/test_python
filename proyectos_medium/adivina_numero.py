from random import randint
nombre = input('Ingresa tu nombre: ')
print(f'Hola {nombre}, vamos a jugar a adivinar un número entre 1 y 100')
numero_a_adivinar = randint(1, 100)

intentos = 0

while intentos < 8:
    intentos += 1
    numero = int(input('Ingresa un número: '))
    if numero < 1 or numero > 100:
        print('El número debe estar entre 1 y 100')
        continue
    if numero < numero_a_adivinar:
        print('El número es mayor')
    elif numero > numero_a_adivinar:
        print('El número es menor')
    else:
        print(f'Felicidades {nombre}, adivinaste el número en {intentos} intentos')
        break
else:
    if intentos == 8:
        print(f'Lo siento {nombre}, no adivinaste el número. El número era {numero_a_adivinar}')
        