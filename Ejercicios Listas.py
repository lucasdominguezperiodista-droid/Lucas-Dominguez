# =========================
# ANALISIS DE VENTAS
# =========================

# 1. Lista de ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Notebook", "cantidad": 2, "precio": 1500.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-02", "producto": "Notebook", "cantidad": 1, "precio": 1500.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 20.0}
]

# -------------------------
# 2. Ingresos totales
# -------------------------
ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# -------------------------
# 3. Ventas por producto
# -------------------------
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0

    ventas_por_producto[producto] += cantidad

# Producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# -------------------------
# 4. Precio promedio por producto
# -------------------------
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)

    suma_precios, total_cantidad = precios_por_producto[producto]
    suma_precios += precio * cantidad
    total_cantidad += cantidad

    precios_por_producto[producto] = (suma_precios, total_cantidad)

# Calcular promedios
precio_promedio = {}

for producto, (suma, cantidad) in precios_por_producto.items():
    precio_promedio[producto] = suma / cantidad

# -------------------------
# 5. Ingresos por día
# -------------------------
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0

    ingresos_por_dia[fecha] += ingreso

# -------------------------
# 6. Resumen de ventas
# -------------------------
resumen_ventas = {}

for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio[producto]
    }

# -------------------------
# RESULTADOS
# -------------------------

print("----- LISTA DE VENTAS -----")
for v in ventas:
    print(v)

print("\n----- INGRESOS TOTALES -----")
print(ingresos_totales)

print("\n----- PRODUCTO MÁS VENDIDO -----")
print(producto_mas_vendido, "-", ventas_por_producto[producto_mas_vendido])

print("\n----- PRECIO PROMEDIO POR PRODUCTO -----")
for p, precio in precio_promedio.items():
    print(p, ":", round(precio, 2))

print("\n----- INGRESOS POR DÍA -----")
for f, ingreso in ingresos_por_dia.items():
    print(f, ":", ingreso)

print("\n----- RESUMEN DE VENTAS -----")
for p, datos in resumen_ventas.items():
    print(p, ":", datos)