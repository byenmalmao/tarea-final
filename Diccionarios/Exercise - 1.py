#Solicitar al usuario el nombre y edad de varias personas
diccionario = input("Digite el nombre y edad de varias personas (Maria,15;Julio,20): ")
dicc_nome = diccionario.split(";")

#Almacenar esta informacion en un diccionario
diccionario_personas = dict()

for par in dicc_nome:
    nombre,edad = par.split(",")
    diccionario_personas[nombre] = int(edad)

#Imprimir el diccionario
print("Diccionario de personas: ", diccionario_personas) 
