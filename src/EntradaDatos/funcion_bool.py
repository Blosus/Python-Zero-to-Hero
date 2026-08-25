# Programa: Funcion Bool

# 1. Numeros (int y float)
print(bool(0)) # False (El vacio numerico)
print(bool(0.0)) # False
print(bool(42)) # True (Existe valor)

# 2. Texto (Strings)
# Cadena Vacia = Nada = False
print(bool("")) # False

# Cadena con espacio o texto = ALgo = True
print(bool(" "))    # True
print(bool("Hola")) # True

# 3. None (Ausencia Total)
vacio = None
print(bool(vacio)) # False
print (bool(False)) # False
print (bool(True)) # True