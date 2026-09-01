class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return (f'Pelicula: {self.nombre}')
