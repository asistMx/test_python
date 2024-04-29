


lista1 = ['Juan', 'Pedro', 'Maria', 'Ana']
lista2 = ['Jose', 'Luis', 'Carlos', 'Ana']
nombres = "Andres,Jacinto,Guillermo,Josue"
lista_nombres = nombres.split(",")


# Sumar o concatenar listas
lista_mezclada = lista1 + lista2 + nombres.split(",")
print(lista_mezclada)

# Extender una lista
print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)

# Agregar un elemento al final de la lista
lista_mezclada.append('Ricardo')

print(lista_mezclada)

# Insertar un elemento en una posicion especifica
lista_mezclada.insert(2, 'Javier')

print(lista_mezclada)

# Eliminar un elemento de la lista
lista_mezclada.remove('Javier')

print(lista_mezclada)

# Eliminar un elemento de la lista por indice

del lista_mezclada[2]

print(lista_mezclada)


# Eliminar el ultimo elemento de la lista
lista_mezclada.pop()

print(lista_mezclada)

# Ordenar una lista
lista_mezclada.sort()

print(lista_mezclada)

lista_al_revez = sorted(lista_mezclada, reverse=True)

print(lista_al_revez)


# Invertir una lista
lista_al_revez.reverse()
print(lista_al_revez)

# Contar elementos en una lista
print(lista_al_revez.count('Ana'))

# Encontrar el indice de un elemento
print(lista_al_revez.index('Ana'))

# Obtener la longitud de una lista
print(len(lista_al_revez))

# Obtener el maximo y minimo de una lista
print(max(lista_al_revez))
print(min(lista_al_revez))

# Obtener la suma de los elementos de una lista
print(sum([1,2,3,4,5,6,7,8,9,10]))

# Obtener la media de los elementos de una lista
print(sum([1,2,3,4,5,6,7,8,9,10])/len([1,2,3,4,5,6,7,8,9,10]))


# Funcion zip
nombres = ['Juan', 'Pedro', 'Maria', 'Ana']
edades = [30, 40, 50, 60]
estaturas = [1.70, 1.80, 1.60, 1.75]

personas = zip(nombres, edades, estaturas)

print(list(personas))

for persona in zip(nombres, edades, estaturas):
    print(persona)



# Copiar una lista
# == compara el contenido de las listas; is compara las referencias de las listas
lista = [1,2,3,4,5,6,7,8,9,10]

lista_cop = lista

print(lista is lista_cop)

lista_copia = lista.copy()

print(lista is lista_copia)