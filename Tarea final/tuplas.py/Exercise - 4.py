#Generar tupla de numeros aleatorios
import random
tupla = tuple(random.randint(1, 100) for _ in range(10))

#Encontrar el menor y el mayor de la tupla
menor = min(tupla)
mayor = max(tupla)

#Imprimir la tupla, el menor y el mayor
print("Tupla de numeros aleatorios: ", tupla)
print("El menor es: ", menor, "\nEl mayor es: ", mayor)
