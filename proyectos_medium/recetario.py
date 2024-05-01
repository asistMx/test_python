from pathlib import Path
from os import system,name, chdir, getcwd
import time



def load_recetas(ruta_recetas):

    recetas = []
    contador = 0
    for archivo in Path(ruta_recetas).glob('**/*.txt'):
            contador += 1
            ruta = archivo
            archivo = archivo.name
            receta = (archivo, ruta)
            recetas.append(receta) 
    return recetas, contador


if __name__ == '__main__':

    while True:
        system('clear')
        print("Bienvenido al recetario".center(50," "))
        ruta_recetas = Path(Path.home(),  'Documents',"recetas")
        print("Nuestras recetas estan en:")
        print(ruta_recetas)
        chdir(ruta_recetas)
        recetas, contador = load_recetas(ruta_recetas)
        
        print("MENU".center(50, "*"))
        print("\n")
        lista_opciones = ["Ver recetas", "Leer receta", "Agregar receta", "Agregar categoria", "Eliminar receta", "Eliminar categoria", "Salir"]    
        for index, opcion in enumerate(lista_opciones):
            print(f"{index + 1}. {opcion}")

        print("\n")
        print("*"*50)
        print("\n")
        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            system('clear')
            
            print(f"Tenemos {contador} recetas")
            for index, receta in enumerate(recetas):
                print(f"{index + 1}. {receta[0]}".replace(".txt",""))
            
            input("Presione enter para continuar")

        if opcion == '2':

            system('clear')
            seleccion = int(input("Ingrese el numero de la receta que desea leer: "))
            if seleccion > 0 and seleccion <= contador:
                with open(Path(ruta_recetas,recetas[seleccion - 1][1])) as archivo:
                    print(archivo.read())
                input("Presione enter para continuar")
            else:
                print("Receta no encontrada")
                time.sleep(2)

        if opcion == '3':

            nombre_categoria = input("Ingrese el nombre de la categoria: ")
            if Path(ruta_recetas, nombre_categoria).exists():
                nombre_receta = input("Ingrese el nombre de la receta: ")
                with open(Path(ruta_recetas,nombre_categoria, f"{nombre_receta}.txt"), "w") as archivo:
                    archivo.write(input("Ingrese la receta: "))
                print("Receta agregada")
                time.sleep(2)
            else:
                 print(f"Categoria {nombre_categoria} no existe") 
                 time.sleep(2)
            
        if opcion == '4':
            nombre_categoria = input("Ingrese el nombre de la categoria: ")
            if not Path(ruta_recetas, nombre_categoria).exists():
                path_categoria = Path(ruta_recetas, nombre_categoria)
                path_categoria.mkdir()
                print(f"Categoria {nombre_categoria} creada")
                time.sleep(2)
            else:
                 print(f"Categoria {nombre_categoria} ya existe") 
                 time.sleep(2)

        if opcion == '5':
            system('clear')
            seleccion = int(input("Ingrese el numero de la receta que desea eliminar: "))
            if seleccion > 0 and seleccion <= contador:
                Path(ruta_recetas,recetas[seleccion - 1][1]).unlink()
                #print(Path(ruta_recetas,recetas[seleccion - 1][1]))
                print("Receta eliminada")
                time.sleep(4)
            else:
                print("Receta no encontrada")
                time.sleep(2)

        if opcion == '6':
            system('clear')
            nombre_categoria = input("Ingrese el nombre de la categoria: ")
            if Path(ruta_recetas, nombre_categoria).exists():
                try:
                    Path(ruta_recetas, nombre_categoria).rmdir()
                    print(f"Categoria {nombre_categoria} eliminada")
                    time.sleep(2)
                except OSError as e:
                    print(f"No se puede eliminar la categoria {nombre_categoria} porque tiene recetas")
                    time.sleep(2)
            else:
                print(f"Categoria {nombre_categoria} no existe") 
                time.sleep(2)

        if opcion == '7':
            break
    
    system('clear')
    print("Programa finalizado")
    
        

    
