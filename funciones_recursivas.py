
def recursiva(valor):
    print(valor)
    if valor == 0:
        return 0
    else:
        new = valor + recursiva(valor - 1)
        print(new)
        return new
    

recursiva(5)

if True:
    print("throwing error")
    raise Exception("Error")