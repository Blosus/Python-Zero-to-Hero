print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAXIMO = 7
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    acumulador_suma += numero
    numero += 1
print(f'\nResultado suma acumulada: {acumulador_suma}')