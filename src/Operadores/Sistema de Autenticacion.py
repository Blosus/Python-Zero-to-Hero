print(f'*** Sistema Autenticacion ***')

user = 'Leah'
password = '67'

usuario = input('Ingresa tu nombre de usuario: ')
contra = input('Ingresa la contrasenia: ')

correcto = (usuario.strip() == user) and (password.strip() == contra)

print(f'Tienes acceso a la cuenta? {correcto}')