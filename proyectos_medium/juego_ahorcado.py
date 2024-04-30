from random import choice

# Leer archivo de palabras
def inicializar_juego():
    palabras = []
    with open('palabras.txt', 'r') as f:
        palabras = f.read().splitlines()
        #print(palabras)
    #Seleccionar una palabra aleatoria
    palabra = choice(palabras).lower()

    # Mostrar la palabra con guiones bajos
    palabra_oculta = ['_'] * len(palabra)
    print(f"{palabra_oculta}")

    return palabra



# 4. Pedir una letra al usuario
def pedir_letra():
    letra = input('Ingresa una letra: ')
    if len(letra) != 1:
        print('Ingresa solo una letra')
        return pedir_letra()
    return letra


# 5. Verificar si la letra esta en la palabra
def validar_letra(letra, palabra_oculta):
    if letra in palabra:
        return True
    return False


# 6. Mostrar la palabra con las letras adivinadas
def mostrar_palabra(palabra,palabra_oculta, letras_adivinadas=[]):
    print(letras_adivinadas)
    for letra in letras_adivinadas:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
        


if __name__ == "__main__":
    palabra = inicializar_juego()
    palabra_oculta = ['_'] * len(palabra)
    
    contador = 0
    vidas = len(palabra)
    letras_adivinadas = []
    while contador < len(palabra):
        contador += 1
        vidas -= 1
        print(f'Vidas {vidas} restantes')
        letra = pedir_letra()
        if validar_letra(letra, palabra):
            print('La letra esta en la palabra')
            letras_adivinadas.append(letra)
            mostrar_palabra(palabra,palabra_oculta, letras_adivinadas)
            print(f"{palabra_oculta}")
        else:
            print('La letra no esta en la palabra')

        if '_' not in palabra_oculta:
            print('Felicidades, adivinaste la palabra')
            break
    else:  
        print(f'Lo siento, no adivinaste la palabra. La palabra era {palabra}')
        