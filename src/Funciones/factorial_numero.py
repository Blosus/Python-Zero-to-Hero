print('*** Factorial del Numero 5 ***')

# Definimos la funcion factorial recursiva
def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else:
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

resultado = factorial_recursiva(5)