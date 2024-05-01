from collections import Counter


lista = [1,1,1,1,1,2,2,2,2,3,3,3,3,2,2,2,4,4,4,45,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6]
frase = "al pan pan y al vino vino"
serie = Counter(lista)
print(Counter(lista))
print(Counter("hola mundo"))
print(Counter(frase.split()))
print(serie.most_common())
print(list(serie))



