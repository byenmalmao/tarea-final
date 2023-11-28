# Desarrolla un programa que, dado un número entero, genere
# una lista de todos los números primos hasta ese número

n = int(input("Ingrese un número: "))
primos = [2]
for i in range(3, n + 1):
    primo = True
    for j in primos:
        if i % j == 0:
            primo = False
            break
    if primo:
        primos.append(i)
print(primos)
