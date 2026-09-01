from src.ManejoArchivos.catalogo_peliculas.pelicula import Pelicula
from src.ManejoArchivos.catalogo_peliculas.servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catalogo Peliculas ***')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar Peliculas
                2. Listar Peliculas
                3. Eliminar catalogo de peliculas
                4. Salir''')
                opcion = int(input('Escribe tu opcion (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Dame el nombre de la pelicula: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print(f'Muchas gracias por usar el programa!')
                    return False
                else:
                    print(f'Opcion incorrecta!')
            except ValueError:
                print(f'Error: Introduce un numero valido')
            except Exception as e:
                print(f'Ocurrio un error: {e}')

# Programa Principal
if __name__ == '__main__':
    catalogo_peliculas = AppCatalogoPeliculas()
    catalogo_peliculas.mostrar_menu()