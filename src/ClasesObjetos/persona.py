# Definicion de una clase
class PersonaPrincipal:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dir. mem self: {id(self)}')
        print(f'Dir. mem self hex: {hex(id(self))}')

# Creacion de Objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = PersonaPrincipal('Rui', 'Veloso') # Crea un objeto vacio en memoria
    persona1.mostrar_persona()
    print(f'Dir. mem personal: {id(persona1)}')
    print(f'Dir. mem hex personal: {hex(id(persona1))}')

    # Creacion un segundo objeto
    persona2 = PersonaPrincipal('Leah', 'Gomez')
    persona2.mostrar_persona()
    print(f'Dir. mem personal: {id(persona2)}')
    print(f'Dir. mem hex personal: {hex(id(persona2))}')