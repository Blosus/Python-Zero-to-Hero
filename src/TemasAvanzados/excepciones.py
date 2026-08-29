print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('EL denominador es igual a 0')

        resultado = numerador / denominador
        print(f'Resultado de la division: {resultado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    else:
        print(f'No ocurrio ningun error.')
    finally:
        print(f'Terminamos de procesor la excepcion')

# Ejemplos de uso
dividir(10, 2)
dividir (10,'0')
