print(f'*** Tienda en Linea ***')

MINIMO = 1000
ES_MIEMBRO = input("Es usted miembro de la tienda? (Si/No) ")
COMPRA = int(input("Ingresa el monto a pagar: "))
Descuento = 0.00

if (COMPRA >= MINIMO and ES_MIEMBRO.strip().lower() == 'si'):
    Descuento = 0.10
elif (ES_MIEMBRO.strip().lower() == 'si'):
    Descuento = 0.05

compra_total = COMPRA - (COMPRA*Descuento)

print(f'''
MIEMBRO: {ES_MIEMBRO}
COMPRA: {COMPRA}
DESCUENTO: {Descuento}
COMPRA CON DESCUENTO {compra_total}''')