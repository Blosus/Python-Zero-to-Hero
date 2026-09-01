class Snack:
    contador_snack = 0

    def __init__(self, nombre= '', precio= 0.0):
        self.nombre = nombre
        self.precio = float(precio)
        Snack.contador_snack += 1
        self.id_snack = Snack.contador_snack

    def __str__(self) -> str:
        return(f'Snack: id_snack = {self.id_snack}, Nombre = {self.nombre},'
               f'Precio = {self.precio}')

    def escribir_snack(self):
        return f'{self.id_snack},{self.nombre},{self.precio}'