print(f'*** Revisar si un numero es Positivo ***')

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print(f'El {numero} es positivo')
elif numero < 0:
    print(f'El {numero} es negativo')
else:
    print(f'El {numero} es cero')