print('*** Regresar una tupla de valores desde una funcion ***')

# Definicion dela funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad )

nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')