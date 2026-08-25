print(f'*** Break y Continue ***')

# Ejemplo con break
print('Palabra Break:')
for numero in range (1, 10):
    if numero % 2 == 0:
        print('Es un numero par')
        break


#Ejemplo con Continue
print('\nPalabra continue: ')
for numero in range (1, 10):
    if numero % 2 == 1:
        continue
    print(numero) # Solo numeros pares