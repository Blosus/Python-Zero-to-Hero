# Manejos de Cadenas

# Dividir una cadena split(
cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

# Buscar y Remplazar
posicion = cadena.find('mundo')
print(f'Posicion de la cadena Mundo: {posicion}')

# Reemplazar con replace
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicacion de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 3
print(f'Resultado multiplicacion de cadenas: {resultado_multiplicacion_cadenas}')

# Strip - Limpiar una cadena

cadena = '  Hola Mundo    '
limpio = cadena.strip()

print(f'Cadena limpia de caracteres al inicio y al final: {limpio}')