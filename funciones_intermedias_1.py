# =========================
# 1. Actualizar valores
# =========================

matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)


# =========================
# 2. Iterar lista de diccionarios
# =========================

def iterarDiccionario(lista):
    for elemento in lista:
        texto = ""
        for clave, valor in elemento.items():
            texto += f"{clave} - {valor}, "
        print(texto.rstrip(", "))


# =========================
# 3. Obtener valores por clave
# =========================

def iterarDiccionario2(llave, lista):
    for elemento in lista:
        if llave in elemento:
            print(elemento[llave])


# =========================
# 4. Diccionario con listas
# =========================

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"\n{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)


# =========================
# PRUEBAS
# =========================

print("\n--- iterarDiccionario ---")
iterarDiccionario(cantantes)

print("\n--- iterarDiccionario2 (nombre) ---")
iterarDiccionario2("nombre", cantantes)

print("\n--- iterarDiccionario2 (pais) ---")
iterarDiccionario2("pais", cantantes)

print("\n--- imprimirInformacion ---")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)