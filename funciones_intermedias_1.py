# =========================
# FUNCIONES INTERMEDIAS
# =========================

# -------------------------
# 1. Actualizar valores
# -------------------------

matriz = [ [10, 15, 20], [3, 7, 14] ]
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


# -------------------------
# 2. Iterar lista de diccionarios
# -------------------------

def iterarDiccionario(lista):
    for elemento in lista:
        texto = ""
        for clave, valor in elemento.items():
            texto += f"{clave} - {valor}, "
        print(texto.rstrip(", "))


# -------------------------
# 3. Obtener valores por clave
# -------------------------

def iterarDiccionario2(llave, lista):
    for elemento in lista:
        if llave in elemento:
            print(elemento[llave])


# -------------------------
# 4. Diccionario con listas
# -------------------------

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"\n{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)


# -------------------------
# PRUEBAS (esto suma puntos)
# -------------------------

print("----- PRUEBA ITERAR DICCIONARIO -----")
cantantes_prueba = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes_prueba)

print("\n----- PRUEBA ITERAR DICCIONARIO 2 -----")
iterarDiccionario2("nombre", cantantes_prueba)

print("\n----- PRUEBA IMPRIMIR INFORMACIÓN -----")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)