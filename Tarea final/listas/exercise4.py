# Diseña un programa que sume los elementos de dos listas
# y cree una nueva lista con los resultados de la suma.

# Solicita las listas al usuario
lista1 = input("Ingrese la primera lista: ")
lista2 = input("Ingrese la segunda lista: ")


lista1 = list(map(int, lista1.split()))
lista2 = list(map(int, lista2.split()))

nueva_lista = []

# Itera sobre las dos listas
for i in range(len(lista1)):
    # Suma los elementos correspondientes
    nueva_lista.append(lista1[i] + lista2[i])

print(nueva_lista)
