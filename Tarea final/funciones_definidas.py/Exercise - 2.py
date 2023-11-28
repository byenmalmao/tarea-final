def fibonacci(n):
    secuencia = []
    secuencia.append(0)
    secuencia.append(1)

    for i in range(2, n):
        secuencia.append(secuencia[i - 1] + secuencia[i - 2])
    return secuencia


print(fibonacci(int(input("Numero a alcanzar: "))))
