# Pedir al usuario los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#Ver si el segundo numero es multiplo del primero
def es_multiplo(num1, num2):
    return num2 % num1 == 0

#Imprimir si es o no el segundo numero multiplo del primero
if es_multiplo(num1, num2):
    print(f"{num2} es múltiplo de {num1}.")
else:
    print(f"{num2} no es múltiplo de {num1}.")
