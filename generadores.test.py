from functools import reduce

def mi_generador():
   
    for i in range(11, 15):
        yield i


rango = iter(range(0, 10))


print(type(rango))
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))

''' for i in rango: 
    print(i) '''
    
    


gen = mi_generador()
try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("Se termino el generador")


# expresion generadoras
lista_generadora = [1,2,3,4,5,6,7,8,9,10]
gen = (i for i in range(0, 10))
print(type(gen))
print(next(gen))
print(next(gen))


gen2 = (i for i in lista_generadora)
print(type(gen2))
print(next(gen2))
print(next(gen2))

lista_pares = [i for i in lista_generadora if i % 2 == 0]

print(lista_pares)

# if ternario

print("Es par" if 10 % 2 == 0 else "Es impar")


#walrus operator

#valid = ((valor := input("Dame un valor: ")) ==  100)
#print(valor)
#print(valid)

def duplicar(x):
    return x * 2

dobles = [duplicar(i) for i in lista_generadora if i % 2 == 0]
print(dobles)

lista_test = [1,2,3,4,5,6,7,8,9,10]

print(list(map(duplicar, lista_test)))

def validar_menor_n(x):
    return x < 5

print(list( filter(validar_menor_n, lista_test)))

print(list(reduce(lambda x, y: x + y, lista_test)))