#Generar contraseña aleatoriamente
import random
import string

def generar_contra(longitud, mayus=True, minus=True, num=True):
    carac = ""
    
    if mayus:
        carac += string.ascii_uppercase #Requisito de letra mayuscula
    if minus:
        carac += string.ascii_lowercase #Requisito de letra minuscula
    if num:
        carac += string.digits #Requisito de numeros

    contraseña = ''.join(random.choice(carac) for _ in range(longitud))
    return contraseña

contra = generar_contra(12, mayus=True, minus=True, num=True)

print("Contraseña generada:", contra) #Imprimir el resultado de la contra
