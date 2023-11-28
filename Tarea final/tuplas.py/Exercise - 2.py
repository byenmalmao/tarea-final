# Escribe un programa que encuentre la intersección de dos tuplas, es decir, los
# elementos comunes entre ambas tuplas.

# Solicita al usuario las dos tuplas
tupla1 = tuple(
    map(int, input("Ingrese la primera tupla separada por comas: ").split(","))
)
tupla2 = tuple(
    map(int, input("Ingrese la segunda tupla separada por comas: ").split(","))
)

# Crea una nueva tupla vacía para almacenar la intersección
interseccion = set(tupla1) & set(tupla2)

# Imprime la intersección
print(interseccion)
