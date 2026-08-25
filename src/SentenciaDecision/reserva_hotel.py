print(f'*** Reserva de Hotel ***')

CUARTO_VISTA = 190.50
CUARTO_SIN_VISTA = 150.50

cliente = input('Nombre del CLiente: ')
dias = int(input('Dias de Estadia: '))
mar = input('Con vista al mar (Si/No)? ')

VISTA_MAR = "Si" if mar.strip().lower() == "si" else "No"

if VISTA_MAR == True:
    total = dias*CUARTO_VISTA
else:
    total = dias*CUARTO_SIN_VISTA


print(f'''-------Detalles de la Reservacion-------
Cliente: {cliente.strip()}
Dias de estadia: {dias}
Costo Total: ${total}
Habitacion con vista al mar: {VISTA_MAR}''')