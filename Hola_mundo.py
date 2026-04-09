# 1. Imprime "Hola, mundo"
print("Hola, mundo")
print("Estoy practicando Git")

# 2. Imprime "Hola, Lucas" con el nombre en una variable
nombre = "Lucas"

print("Hola,", nombre)              # con coma
print("Hola, " + nombre)           # con +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156

print("Hola", numero, "!")         # con coma
print("Hola " + str(numero) + "!") # con + (convertimos a string)

# 4. Imprimir comidas favoritas
comida1 = "tacos"
comida2 = "arepas"

print("¡Me encanta comer {} y {}!".format(comida1, comida2))  # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!")            # con f-string