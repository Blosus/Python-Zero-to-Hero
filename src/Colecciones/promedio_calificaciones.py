print('*** Promedio de Calificaciones ***')

total_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar: '))
calificaciones = []

# iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificacion[{indice}] = '))
    calificaciones.append(calificacion)

# Imprimimos las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

# calculamos el promedio de las calificaciones
# sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones/total_calificaciones
print(f'\nPromedo de las calificaciones: {promedio}')