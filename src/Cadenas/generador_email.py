# Crea un programa para generar un email a partir de los siguientes datos:
print('*** Generador de Emails ***')

# Nombre completo del usuario
nombre_completo = " Rui Manuel Veloso Ramirez "
print(f"Nombre Usuario: {nombre_completo}")

# Ahora nos toca procesar o normalizar el nombre de usuario
# Limpiamos los espacios en blanco al inico y al final
nombre_usuario = nombre_completo.strip()

# Reemplazar los espacios en blanco por puntos y Convertimos en Minusculas
nombre_usuario = nombre_usuario.replace(" ", ".").lower()
print(f"Nombre Usuario Normalizado: {nombre_usuario}")


# Datos de la Empresa
nombre_empresa = 'Global Mentoring'
print(f'Nombre Empresa: {nombre_empresa}')
extension_dominio = '.com.mx'
print(f'Extension del Domino: {extension_dominio}')

# Quitamos los espacios en blanco y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'

print(f'\nDominio del Email Normalizado: {dominio_email_normalizado}')

email = f'{nombre_usuario}{dominio_email_normalizado}'
print(f'Email Final Generado: {email}')

