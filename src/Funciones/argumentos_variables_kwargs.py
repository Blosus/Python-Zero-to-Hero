# *args - arguments = tupla
# **kwargs - keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas Info: {kwargs}')

# Llamamos la funcion
superheroe_superpoderes('Spider-Man', 'Instinto Aracnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Iron Man', 'Armadura', 'Playboy', edad=45)