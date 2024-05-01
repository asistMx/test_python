from os import system
import time





def generador_farmacia():
    print("Generando turnos de farmacia".center(50, " "))
    for n in range(1, 1000):
        yield n


def generador_perfumeria():
    print("Generando turnos de perfumeria".center(50, " "))
    for n in range(1, 1000):
        yield n
    
def generador_cosmeticos():
    print("Generando turnos de cosmeticos".center(50, " "))
    for n in range(1, 1000):
        yield n

def atender_turno():
    pass

def mostrar_turnos():
    pass







if __name__ == "__main__":

    turno_farmacia_gen = generador_farmacia()
    turno_perfumeria_gen = generador_perfumeria()
    turno_cosmeticos_gen = generador_cosmeticos()
    

    while True:

  
        Areas = ["Farmacia", "Perfumeria", "Cosmeticos"]
        system('clear')
        print("Bienvenido al sistema de turnos".center(50, " "))
        print("Areas".center(50, " "))
        for index, area in enumerate(Areas):
            print(f"{Areas.index(area) + 1}. {area}")
        print("4. Salir")
        seleccion = int(input("Seleccione que area visita: "))

        if seleccion == 1:
            system('clear')
            print("Ha seleccionado Farmacia")
            turno_farmacia = next(turno_farmacia_gen)
            print(f"Su turno es el {turno_farmacia}")
            time.sleep(1)
        
        if seleccion == 2:
            system('clear')
            print("Ha seleccionado Perfumeria")
            turno_perfumeria = next(turno_perfumeria_gen)
            print(f"Su turno es el {turno_perfumeria}")
            time.sleep(1)
        
        if seleccion == 3:
            system('clear')
            print("Ha seleccionado Cosmeticos")
            turno_cosmeticos = next(turno_cosmeticos_gen)
            print(f"Su turno es el {turno_cosmeticos}")
            time.sleep(1)

        if seleccion == 4:
            break



