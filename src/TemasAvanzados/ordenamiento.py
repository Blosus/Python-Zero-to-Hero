print('*** Ordenamiento en Python ***')

# Sintaxis: sorted(iterable, key = None, reverse = False)

empleado = ['Juan', 'Pedro', 'Maria']
# Ordenar la lista
# empleado_ordenados = sorteo(empleados, reverse = True)
empleado_ordenados = sorted(empleado)
print(f'Empleados ordenados: {empleado_ordenados}')

# Ordenar un diccionario (una llave)
empleados_dict = [
    {'nombre':'Juan', 'salario': 3000},
    {'nombre':'Maria','salario':2500},
    {'nombre':'Pedro','salario':3500}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'Empleados ordenados por salario: {empleados_ordenados_por_salario}')