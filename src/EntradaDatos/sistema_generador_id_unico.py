print('*** Sistema Generador ID Unico***')

from random import randint
nombre = input('Cual es tu nombre? ')
apellido = input('Cual es tu apellido? ')
nacer = input('Cual es tu anio de nacimiento (YYYY)? ')
rand = randint(1000,9999)

ID = f'{(nombre[0:2].upper())}{(apellido[0:2].upper())}{nacer[-2:]}{rand}'


print(f'Hola {nombre},\n'
      f'\tTu nuevo numero de indentificacion (ID) generado por el sistema es:\n'
      f'\t{ID}\n'
      f'\tFelicidades!\n')