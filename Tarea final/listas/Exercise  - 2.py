#Palabras ingresadas por el usuario
palabra = input("Ingresa las palabras a invertir separadas por comas: ")
lista_palabras = list(palabra.split(","))

#Invertir el orden de la lista
invert = lista_palabras[::-1]

#Imprimir la lista invertida
print("La palabras invertidas son:", invert)
