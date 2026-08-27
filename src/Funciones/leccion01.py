def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutar la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto de impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)

print(f'Pago con impuesto: {pago_con_impuesto}')