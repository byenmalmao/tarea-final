#Solicitar al usuario claves y valores para el diccionario
diccionario = input("Digite las claves y valores de esta manera (Año,2023;Marca,Ford): ")
dicc_nomed = diccionario.split(";")

dicc = dict() #Almacenar las claves y valores en un diccionario

for par in dicc_nomed:
    clave, valor = par.split(",")
    dicc[clave] = valor

print("Diccionario: ", dicc) #Imprimir el diccionario

dicc_del = input("Cual elemento desea borrar (Año,2023): ") #Pedir al usuario que elimine un elemento
clave_borrar, valor_borrar = dicc_del.split(",")

if clave_borrar in dicc: #Si el elemento esta en el diccionario se eliminara
    del dicc[clave_borrar]
    print("Diccionario actualizado: ", dicc) #Imprimir el diccionario actualizado
else:
    print("El elemento no existe")