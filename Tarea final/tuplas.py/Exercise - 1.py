# Crea un programa que solicite al usuario dos tuplas de números, las concatene y luego
#  imprima la tupla resultante.
# Solicitar la primera tupla al usuario
tupla1 = tuple(
    map(int, input("Ingrese la primera tupla separada por comas: ").split(","))
)

# Solicitar la segunda tupla al usuario
tupla2 = tuple(
    map(int, input("Ingrese la segunda tupla separada por comas: ").split(","))
)

# Concatenar las dos tuplas
tupla_concatenada = tupla1 + tupla2

# Imprimir la tupla concatenada
print(tupla_concatenada)
