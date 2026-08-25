# Programa: Reemplazar textos en python

mensaje = "Hola Mundo, Mundo"

# Reemplazar TODAS las apariciones
nuevo = mensaje.replace("Mundo", "Python")
print(nuevo)
# Salida: "Hola Python, Python"

# Reemplazar solo UNA vez
uno_solo = mensaje.replace("Mundo", "Dev", 1)
print(uno_solo)
# Saliida
