print('*** Repeticion de un Mensaje ***')

mensaje = input('Proporcionar un mensaje a repetir: ')
numero_de_repeticiones = int(input('Proporciona el numero de repeticiones: '))

# Iterar sobre el rango de repeticiones
for i in range(numero_de_repeticiones):
    print(f'{i+1} - {mensaje}')