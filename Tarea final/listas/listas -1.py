#Solicitar al usuario una lista de numeros
numeros = input("Digita una lista de numeros separados por comas: \n")
lista_numeros = list(int(numero) for numero in numeros.split(','))

#Encontrar el menor y el mayor de la lista
menor = min(lista_numeros)
mayor = max(lista_numeros)

#Imprimir ambos valores
print("El menor de la lista es: ", menor)
print("El mayor de la lista es: ", mayor)