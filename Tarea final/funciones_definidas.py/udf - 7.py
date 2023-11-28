#Pedir al usuario las informaciones necesarias para calcular interes de prestamo
monto = float(input("Monto prestado: "))
tiempo = int(input("Duracion del prestamo en meses: "))
interes = float(input("Interes del prestamo: "))

#Calcular el interes simple y la cuota mensual
paga = monto / tiempo
intereses = monto * (interes / 100)
monto = paga + intereses

#Imprimir la cuota mensual
print(f"Cuota Mensual: {monto}")