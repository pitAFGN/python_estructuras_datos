ventas = [
    {"nombre": "Laptop", "precio": 1200, "unidades": 3, "categoria": "Tecnologia"},
    {"nombre": "Mouse", "precio": 25, "unidades": 10, "categoria": "Tecnologia"},
    {"nombre": "Silla", "precio": 150, "unidades": 2, "categoria": "Hogar"},
    {"nombre": "Libro", "precio": 20, "unidades": 15, "categoria": "Educacion"},
    {"nombre": "Audifonos", "precio": 80, "unidades": 5, "categoria": "Tecnologia"},
    {"nombre": "Dildo", "precio": 50, "unidades": 20, "categoria": "Hogar"},
]

# 1. List comp: valor_total por producto
valores_totales = [
    producto["precio"] * producto["unidades"]
    for producto in ventas
]

# 2. List comp con filtro: productos con valor_total > 1000
productos_caros = [
    producto["nombre"]
    for producto in ventas
    if producto["precio"] * producto["unidades"] > 1000
]

# 3. Dict comp: nombre → {valor, unidades}
producto_info = {
    producto["nombre"]: {
        "valor": producto["precio"] * producto["unidades"],
        "unidades": producto["unidades"]
    }
    for producto in ventas
}

# 4. Dict comp con filtro: precio > 50
ranking_premium = {
    producto["nombre"]: producto["precio"] * producto["unidades"]
    for producto in ventas
    if producto["precio"] > 50
}

# Ordenado por valor desc
ranking_ordenado = dict(
    sorted(ranking_premium.items(), key=lambda x: x[1], reverse=True)
)

# 5. Set comp
categorias_unicas = {
    producto["categoria"]
    for producto in ventas
}

productos_baratos = {
    producto["nombre"]
    for producto in ventas
    if producto["precio"] <= 50
}

# 6. Combinar
gran_total = sum(
    producto["precio"] * producto["unidades"]
    for producto in ventas
)

resumen_formateado = [
    f"{producto['nombre']} -> {producto['precio'] * producto['unidades']}"
    for producto in ventas
]

# Resultados
print("Valores totales:", valores_totales)
print("Productos caros:", productos_caros)
print("Info productos:", producto_info)
print("Ranking premium:", ranking_ordenado)
print("Categorias únicas:", categorias_unicas)
print("Productos baratos:", productos_baratos)
print("Gran total:", gran_total)
print("Resumen:", resumen_formateado)