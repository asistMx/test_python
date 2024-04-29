from dataclasses import dataclass


@dataclass
class Persona:
    nombre: str
    edad: int
    raza: str = 'Humano'

  
     
persona = Persona('Jose', 30)

print(persona.__dict__)



