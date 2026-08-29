from functools import reduce

from src.Ciclos import suma_acumulativa

print('*** Funciones Lambda ***')

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de: {cuadrado(5)}')

# Funcion lambda (anonima)

cuadrado2 = lambda x: x**2
print(f'El cuadrado es: {cuadrado2(5)}')

# Con map y lambda
# Creamos una lista de numeros
numeros = [1, 2, 3, 4, 5]

# Aplicar una funcion lambda para obtener el cuadradp de cada numero
cuadrados = list(map(lambda x: x**2, numeros))
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de usar filter para filtrar numeros pares: {pares}')

# Reduce y Map
suma_acumulativa = reduce(lambda x, y: x + y, numeros)
print(suma_acumulativa)