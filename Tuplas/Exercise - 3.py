# Crea un programa que tome una lista de nombres y sus edades, y
# luego cree una tupla para cada persona (nombre, edad).
# Finalmente, imprime la lista de tuplas resultante.

# Solicita los nombres y edades al usuario
nombres = input("Ingrese los nombres separados por comas: ").split(",")
edades = input("Ingrese las edades separadas por comas: ").split(",")

# Crea una nueva lista de tuplas
tuplas = [(nombre, edad) for nombre, edad in zip(nombres, edades)]

# Imprime la lista de tuplas
print(tuplas)

etoces= 23
