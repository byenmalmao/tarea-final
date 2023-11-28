#Solicitar al usuario una lista de numeros
lista = input("Ingresa una lista de numeros separados por comas: ")
lista_numeros = lista.split(",")

#Eliminar elementos duplicados de la lista
conjunto = set(lista_numeros)
lista_sin = list(conjunto)

#Imprimir la lista sin elementos duplicados
print("Lista de numeros sin repetir: ", lista_sin)
