print('*** Listas y Diccionarios ***')

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista:
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
for contador, personas in enumerate(personas):
    print(f'{contador+1} - Persona: {personas}')