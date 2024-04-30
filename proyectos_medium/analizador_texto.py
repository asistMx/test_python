

texto = input("Introduce un texto: ")
texto_buscar = input("Introduce 3 caracteres separados por coma: ")

# Contar el número de palabras
def contar_palabras(texto):
    return len(texto.split())

# Contar el número de letras
def contar_letras(texto):
    return len(texto.replace(" ", ""))

# Contar el número de veces que aparece un texto
def contar_texto(texto, texto_buscar):
    list_buscar = texto_buscar.split(',')
    print(list_buscar)
    apariciones= []
    for i in list_buscar:
        print(i)
        veces = texto.count(i)
        apariciones.append((i, veces))
    return apariciones

def encotrar_inicio_fin(texto):
    inicio = texto[0]
    fin = texto[-1]
    return inicio, fin

def voltear_texto(texto):
    return texto[::-1]


print(contar_palabras(texto))
print(contar_letras(texto))
print(contar_texto(texto, texto_buscar))
print(encotrar_inicio_fin(texto))
print(voltear_texto(texto))