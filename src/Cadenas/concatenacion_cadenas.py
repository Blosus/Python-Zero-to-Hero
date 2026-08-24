# Programa: Ejemplo de concatenacion de cadenas

#1. Usando el Operador +
nombre = "Rui"
apellido = "Veloso"
nombre_completo = nombre + " " + apellido

print("Usando + : " + nombre_completo)

#2. Usando el metodo print
edad = 20
print("Usando comas:","Nombre: ", nombre_completo, ", Edad: ", edad)

# 3. Usando F-Strings
ciudad = "Mazatlan"
pais = "Mexico"
profesion = "Ingeniero"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)