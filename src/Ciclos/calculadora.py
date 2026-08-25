print('*** Calculadora en Python ***')

salir = False
while not salir:
    print(f'''\nOperaciones que puedes realizar:
    \t1. Suma
    \t2. Resta
    \t3. Multiplicacion
    \t4. Division
    \t5. Salir''')
    Opcion = int(input('Escoje una opcion: '))


    if 1 <= Opcion <= 4:
        numero1 = int(input('Dame el valor 1: '))
        numero2 = int(input('Dame el valor 2: '))

    if Opcion == 1:
        print(f'El resultado de la suma es {numero1 + numero2}')
    elif Opcion == 2:
        print(f'El resultado de la resta es {numero1 - numero2}')
    elif Opcion == 3:
        print(f'El resultado de la multi es {numero1 * numero2}')
    elif Opcion == 4:
        print(f'El resultado de la division es {numero1 // numero2}')
    elif Opcion == 5:
        print(f'Hasta luego!')
        salir = True
    else:
        print(f'Opcion invalida!')
