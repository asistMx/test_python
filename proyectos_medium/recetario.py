from pathlib import Path
from os import system,name, chdir, getcwd
import time



def mostrar_recetas(ruta_recetas):

    contador = 0
    for archivo in Path(ruta_recetas).glob('**/*.txt'):
            contador += 1
            archivo = archivo.name
            print(f"{contador}. {archivo}")

    #time.sleep(5)    







if __name__ == '__main__':

    
    while True:
        system('cls')
        #print(name)
        print("Bienvenido al recetario")
        ruta_recetas = Path(Path.home(),  'Documents',"recetas")
        print("Nuestaras recetas estan en:")
        print(ruta_recetas)
        chdir(ruta_recetas)
        #print(getcwd())
        
        
        print("1. Ver recetas")
        print("2. Leer receta")
        print("3. Agregar receta")
        print("4. Agregar categoria")
        print("5. Eliminar receta")
        print("6. Eliminar categoria")
        print("7. Salir")

      



        opcion = input("Ingrese una opcion: ")
        if opcion == '1':
            mostrar_recetas(ruta_recetas)
        if opcion == '7':
            break
    
    system('cls')
    print("Progrma finalizado")
    
        

    
