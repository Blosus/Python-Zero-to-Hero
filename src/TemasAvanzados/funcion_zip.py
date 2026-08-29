from src.Cadenas.concatenacion_cadenas import ciudad

nombre = ['Juan', 'Maria', 'Pedro']
edades = [30, 25, 35]
ciudades = ['Madrid', 'Barcelano', 'Sevilla']

# Combinar los elemenentos correspondientes usando la funcon zip
personas = zip(nombre, edades, ciudades)

# Iterar sobre el resultado de la funcion zip:
for persona in personas:
    print(persona)

