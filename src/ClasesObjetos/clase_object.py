class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona:
        Nombre = {self.nombre}
        Apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}'''


# Codigo Principal
persona1 = Persona('Rui', 'Veloso')
print(persona1) # El metodo __str__ se llama automaticamente desde print
# print(persona1.__str__()) esto es un metodo opcional