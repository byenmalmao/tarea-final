#Pedir al usuario ingresar el numero de su tarjeta
numero_tarjeta = input("Ingresa el numero de tu tarjeta: ")

#Verificar si el numero es valido por medio del algoritmo de LUHN
def luhn_valido(numero):
    digitos = [int(d) for d in str(numero)]

    for i in range(len(digitos) - 2, -1, -2):
        digitos[i] *= 2
        if digitos[i] > 9:
            digitos[i] -= 9

    suma_total = sum(digitos)
    return suma_total % 10 == 0

valido = luhn_valido(numero_tarjeta)

#Imprimir si el numero es valido o no
if valido:
    print(f"El número {numero_tarjeta} es válido.")
else:
    print(f"El número {numero_tarjeta} NO es válido.")
