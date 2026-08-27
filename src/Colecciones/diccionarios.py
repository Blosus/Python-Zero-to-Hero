print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre' : 'Rui',
    'edad' : 20,
    'ciudad':'Mexico'
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}')

# Modificar un valor del diccionario
persona['edad'] = 21
print(f'Diccionario de persona: {persona['edad']}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion', None)
print(f'Diccionario de persona: {persona}')

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')


# Obtener los valores
for valor in persona.values():
    print(f'- Valor: {valor}')

# Obtener las llaves
print(f'Impresion de las llaves del diccionario:')
for llave in persona.keys():
    print(f'- {llave}')