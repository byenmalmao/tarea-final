productos = {
    "leche": 90.0,
    "pan": 5.00,
    "huevos": 6.00,
    "carne": 5.00,
    "frutas": 50.00,
    "vegetales": 60.00,
}

# Solicita la lista de productos al usuario
productos_pedidos = input("Ingrese la lista de productos separados por comas: ").split(
    ","
)


precio_total = 0.0

for producto in productos_pedidos:
    if producto in productos:
        precio_producto = productos[producto]
        precio_total += precio_producto

# Imprime el precio total
print("El precio total es:", precio_total)
