from src.Cadenas.generador_email import nombre_usuario

print(f'*** Aplicacion de Salud y FItness ***')

# Constanted
METAS_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.4 # Valor aproximado, son kilocalorias

# Pedimos los valores al usuario
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

# Verificar si el usaurio alcanzo la meta de pasos diarios
meta_alcanzada = pasos_diarios >= METAS_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la informacion
print(f'''
Usuario: {nombre_usuario}
Pasos dados hoy: {pasos_diarios}
Calorias quemadas: {calorias_quemadas}
Meta de pasos diarios alcanzada: {meta_alcanzada_txt}
La meta de paso diario es de {METAS_PASOS_DIARIOS} pasos''')