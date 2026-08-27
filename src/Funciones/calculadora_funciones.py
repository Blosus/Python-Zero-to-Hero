print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    return int(input('Escoge una opcion: '))

def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operaciones(opcion, salir):
    # Solicitar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: # Sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma: {resultado}\n')
    elif opcion == 2: # Restar
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3: # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4: # Division
        resultado = operando1 / operando2
        print(f'El resultado de la division es: {resultado}\n')
    elif opcion == 5: # Salir
        print('Saliendo del programa de calculadora, hasta pronto!')
        salir = True

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operaciones(opcion, salir)