
from random import *



print(randint(1, 100))
print(random())
print(round(uniform(1, 100),1))
print(choice([1,2,3,4,5,6,7,8,9,10]))
print(choices([1,2,3,4,5,6,7,8,9,10], k=3))
print(sample([1,2,3,4,5,6,7,8,9,10], k=3))
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)