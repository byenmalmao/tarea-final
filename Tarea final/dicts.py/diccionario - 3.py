#Pedir al usuario las claves y valores de dos diccionarios
dicc1 = input("Digite el primer diccionario (Año,2023;Marca,Ford): ")
dicc2 = input("Digite el segundo diccionario (Año,2023;Marca,Ford): ")

dicc_nomed1 = dicc1.split(";")
dicc_nomed2 = dicc2.split(";")

#Almacenar en diccionarios
dicc1 = dict()
dicc2 = dict()

for par in dicc_nomed1:
    clave, valor = par.split(",")
    dicc1[clave] = valor

for par in dicc_nomed2:
    clave, valor = par.split(",")
    dicc2[clave] = valor

resultado = {**dicc1, **dicc2} #Unir los dos diccionarios

print("Diccionario: ", resultado) #Imprimir el resultado