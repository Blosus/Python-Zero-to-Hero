print('*** Imprimir del 1 al 5 de formar recursiva ***')

# Definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')
    else: # Caso Recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

funcion_recursiva(30)