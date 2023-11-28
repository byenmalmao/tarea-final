# Diseña un programa que cuente la frecuencia de cada letra en una cadena de texto y
#  almacene los resultados en un diccionario.

# Solicita la cadena de texto al usuario
cadena_texto = input("Ingrese una palabra: ")

# Crea un diccionario vacío para almacenar las frecuencias
frecuencias = {}

# Itera sobre la cadena de texto
for letra in cadena_texto:
    # Si la letra ya está en el diccionario, incrementa su frecuencia
    if letra in frecuencias:
        frecuencias[letra] += 1
    # De lo contrario, crea una nueva entrada en el diccionario con la frecuencia 1
    else:
        frecuencias[letra] = 1

# Imprime el diccionario de frecuencias
print(frecuencias)
