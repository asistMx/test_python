

class Persona:
    # Atributo de clase
    raza = 'Humano'
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre}'
    
    def __repr__(self):
        return f'{self.nombre}'
    

    


jose = Persona('Jose', 30)

print(jose)
print(jose.raza)

juan = Persona('Juan', 40)
print(juan)
print(juan.raza)



Persona.raza = 'Gato'

print(jose.raza)
print(juan.raza)

print(jose.__dict__)
print(juan.__dict__)
print(repr(jose))
