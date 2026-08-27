print('*** Potencia numero usando funciones recursivas ***')

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
print(potencia(2, 3))