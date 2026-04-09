#-----------------------------------
#Analisis de ventas
#-----------------------------------

#-----------------------------------
#1 Lista de ventas
#-----------------------------------

ventas = [
    { "fecha": "2025-02-01", "producto": "Laptop", "cantidad": 2, "precio": 1200.00 },
    { "fecha": "2025-02-03", "producto": "Telefono", "cantidad": 6, "precio": 750.00 },
    { "fecha": "2025-02-05", "producto": "Tablet", "cantidad": 3, "precio": 500.00 },
    { "fecha": "2025-02-07", "producto": "Monitor", "cantidad": 4, "precio": 300.00 },
    { "fecha": "2025-02-10", "producto": "Teclado", "cantidad": 10, "precio": 50.00 }
]

#-----------------------------------
#2 Ingreso totales
#------------------------------------

total_ingresos = 0
for venta in ventas:
    total_ingresos += venta["cantidad"] * venta["precio"]
print(f"total ingresos: {total_ingresos}")

#-----------------------------------
#3 Producto mas vendido
#-----------------------------------

venta_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in venta_por_producto:
        venta_por_producto[producto] += venta["cantidad"]
    else:
        venta_por_producto[producto] = venta["cantidad"]
producto_mas_vendido = max(venta_por_producto, key=venta_por_producto.get)
print(f"Producto mas vendido: {producto_mas_vendido} con {venta_por_producto[producto_mas_vendido]}")


#-----------------------------------
#4 Precio por producto
#-----------------------------------

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    precio = venta["precio"]
    cantidad = venta["cantidad"]

    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)

    suma_precios, total_unidades = precios_por_producto[producto]
    suma_precios += precio * cantidad
    total_unidades += cantidad

    precios_por_producto[producto] = (suma_precios, total_unidades)

print("Precio promedio por producto:")
for producto, (suma, cantidad) in precios_por_producto.items():
    promedio = suma / cantidad
    print(f"{producto}: {promedio}")



#-------------------------------------
#5 Venta por dia
#-------------------------------------

venta_por_dia = {}
for venta in ventas:
    fecha = venta['fecha']
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha in venta_por_dia:
        venta_por_dia[fecha] += ingreso
    else:
        venta_por_dia[fecha] = ingreso

print("Venta por día:")
for fecha, ingreso in venta_por_dia.items():
    print(f"{fecha} - Ingreso: {ingreso}")

#-------------------------------------
#6 Representacion de datos
#-------------------------------------

resumen_ventas = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0
        }

    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += cantidad * precio

# calcular precio promedio
for producto in resumen_ventas:
    ingresos = resumen_ventas[producto]["ingresos_totales"]
    cantidad = resumen_ventas[producto]["cantidad_total"]
    resumen_ventas[producto]["precio_promedio"] = ingresos / cantidad

print("Resumen de ventas:")
for producto, datos in resumen_ventas.items():
    print(producto, datos)