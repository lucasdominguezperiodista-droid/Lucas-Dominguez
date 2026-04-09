# 1. Básico: imprime todos los números enteros del 0 al 100
print("Ejercicio 1:")
for i in range(0, 101):
    print(i)

print("\n-----------------\n")

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("Ejercicio 2:")
for i in range(2, 501, 2):
    print(i)

print("\n-----------------\n")

# 3. Contando Vanilla Ice
print("Ejercicio 3:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

print("\n-----------------\n")

# 4. Wow. Número gigante a la vista
print("Ejercicio 4:")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("La suma total es:", suma)

print("\n-----------------\n")

# 5. Regrésame al 3
print("Ejercicio 5:")
for i in range(2024, 0, -3):
    print(i)

print("\n-----------------\n")

# 6. Contador dinámico
print("Ejercicio 6:")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)