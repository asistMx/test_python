# Closure : Un closure es una funcion que puede o no recibir argumentos y que retorna otra funcion y los argumentos que recibe los coloca como si recordara el estado.



def funcion_closure(x):
    def funcion_interna(y):
        return x + y
    return funcion_interna



mi_closure = funcion_closure(10)

print(mi_closure(5))
print(mi_closure(25))


# Closure con lambda

closure_lambda = lambda x: lambda y: x + y

mi_closure_lambda = closure_lambda(10)

print(mi_closure_lambda(5))
print(mi_closure_lambda(25))