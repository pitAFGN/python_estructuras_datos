inventario = [
    ["manzana", 10, 2.5],
    ["arroz", 5, 5],
    ["huevos", 16, 7.5]
]

#añade un producto o lo suma a los que ya estan agregados
def añadir_producto (nombre, cantidad, precio):
    existente = False

    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            existente = True
    
    if not existente:
        inventario.append([nombre, cantidad, precio])

#actualiza el precio de un producto ya registrado
def actualizar_precio (nombre, precio_nuevo):

    for producto in inventario:
       if producto[0] == nombre:
            producto[2] = precio_nuevo

#registrar venta o mostrar si no hay la cantidad suficiente
def registrar_venta (nombre, cantidad):
    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad:
                producto[1] -= cantidad
            else:
                print("no hay suficientes tio")
#imprime el inventario en la consola
def mostrar_inventario ():
    for producto in inventario:
       print("nombre: ", producto[0])
       print("cantidad: ", producto[1])
       print("precio: ", producto[2])

añadir_producto("leche", 8, 3.5)
print(inventario)
actualizar_precio("leche", 4)
print(inventario)
registrar_venta("leche", 4)
print(inventario)
mostrar_inventario()