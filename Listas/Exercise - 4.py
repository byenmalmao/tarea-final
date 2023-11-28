lista1 = input("Ingrese la primera lista: ")
lista2 = input("Ingrese la segunda lista: ")

lista1 = list(map(int, lista1.split()))
lista2 = list(map(int, lista2.split()))

nueva_lista = []

for i in range(len(lista1)):
    
    nueva_lista.append(lista1[i] + lista2[i])

print(nueva_lista)
