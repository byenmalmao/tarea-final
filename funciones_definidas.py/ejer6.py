def contar_palabras_unicas(cadena_texto):
    cadena = cadena_texto.lower()
    palabras = cadena.split()
    palabras_unicas = set(palabras)

    return len(palabras_unicas)


print(contar_palabras_unicas(input("Ingrese una oracion: ")))
