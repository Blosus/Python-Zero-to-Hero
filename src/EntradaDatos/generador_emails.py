print('*** Sistema Generador de Emails ***')

nombre = input('Ingresa el Nombre (Ej. Rui Manuel): ')
apellidos = input('Ingresa el Apellido (Ej. Veloso Ramierz): ')
empresa = input('Ingresa el Nombre de la Empresa (Ej. Global Mentoring): ')
dominio = input('Ingresa Extension de Dominio (Ej. \'.com.mx\'): ')

nombre_normalizado = nombre.strip().lower().replace(" ",".") + "." + apellidos.strip().lower().replace(" ",".")

email = f'{nombre_normalizado}@{empresa.lower().strip().replace(" ", "")}{dominio.strip().lower()}'

print(f'\nTu nuevo mail generado por el sistema es:\n'
      f'\t{email}\n'
      f'\tFelicidades!')