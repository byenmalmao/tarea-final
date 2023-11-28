def calcular_potencia(base, exponente):
    resultado = base**exponente
    return resultado


base = int(input("base: "))
exponente = int(input("Exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")
