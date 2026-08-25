# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Basico [Inicio:Fin]
print(texto[0:4]) # "PROG" (El indice 4 no se incluye)

# 2. Atajo desde el inicio [:Fin]
print(texto[:4]) # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [inicio:]
print(texto[8:]) # "CION" (Hasta el ultimo char)

# 4. Indices Negativos
print(texto[-4:]) # "CION" (Los ultimos 4)

#5 Pasos [:Paso] (Invertir Cadena)
print(texto[::-1]) #"NOICAMARGORP"

