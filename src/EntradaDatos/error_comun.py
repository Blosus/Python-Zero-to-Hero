# Programa: Entrada Datos Python
nombre = input("Proporciona tu nombre: ")
print(f"Tu nombre es {nombre}")

# Cuidado con la conversion de tipos al trabajar con valores numericos
# Forma Correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = int(input("Tu edad: "))
print(f"Tu edad es: {edad}")
print(edad + 5) # Funciona (20 + 5 = 25)

# Para decimales (precio, altura)
altura = float(input("Tu altura: "))
print(f"Tu altura es: {altura}")