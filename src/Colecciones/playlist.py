print('*** Playlist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento

for indice in range(numero_canciones):
    cancion = input(f'Proporcione la cancion {indice +1}: ')
    lista_reproduccion.append(cancion)


# Empezamos a agregar canciones
lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream On - Aerosmith')

# Ordenar la lista en orden alfabetico. Sort
lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f'\nLista de reproduccion en orden alfabetico: ')
print(lista_reproduccion)

# Mostrar la lista lista iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')