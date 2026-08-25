# Revisar si una variable se encuentra dentro de rango entre 1 y 10
dato = int(input('Proporciona un dato entero: '))

# Revisamos si esta dentro de rango
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable esta dentro de rango (entre 1 y 10?): {esta_dentro_rango}')

esta_fuera_rango = not(1 <= dato <= 10)
print(f'Variable esta fuera de rango (entre 1 y 10)?: {esta_fuera_rango}')