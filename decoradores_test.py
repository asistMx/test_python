

def funcion_decoradora(funcion_a_decorar):
    def funcion_interna(*args, **kwargs):
        print("Vamos a ejecutar la funcion")
        print(args)
        print(kwargs)
        funcion_a_decorar(*args, **kwargs)
        print("Se ejecuto la funcion")
    return funcion_interna




@funcion_decoradora
def suma(a, b, *args, **kwargs):
    print(a + b)


suma(10, 20,100, 200,nombre="Juan", apellido="Perez")





def decorador_clase(cls):

    print("Vamos a decorar la clase")
    print(cls)
    return cls


class MiClaseDecorada:

    def __init__(self):
        print("Se creo la clase")



mi_clase = MiClaseDecorada()