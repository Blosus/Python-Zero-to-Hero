class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa Principal
if __name__ == '__main__':
    print(f'*** Atributos de Clase ***')
    print(f'Atributp de Clase: {Persona.atributo_clase}')

    Persona.atributo_clase = 10

    print(f'Atributp de Clase: {Persona.atributo_clase}')
