print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Rui', 'Veloso', 20)

# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Rui', apellido='Veloso', edad='20')

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido='Veloso', nombre='Rui')

# Argumentos con valor por default
imprimir_persona(nombre='Rui')