#Solicitar al usuario una cadena de palabras
tupla = input("Ingresa una cadena de palabras separadas por comas: ")
palabras = tupla.split(",")

#Convertir las palabras en tupla
tupla_cadenas = tuple(palabras)

#Separar cada elemento con un espacio
cadena_resultante = ' '.join(tupla_cadenas)

#Imprimir la tupla y la cadena resultante
print("Tupla ingresada:", tupla_cadenas)
print("Cadena resultante:", cadena_resultante)
