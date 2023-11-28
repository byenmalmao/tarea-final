#Pedir al usuario ingresar un numero
numero = int(input("Ingrese un número para calcular su factorial: "))

#Calcular el factorial del numero
def factorial_for(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

resultado = factorial_for(numero)

print(f"El factorial de {numero} es: {resultado}") #Imprimir el resultado