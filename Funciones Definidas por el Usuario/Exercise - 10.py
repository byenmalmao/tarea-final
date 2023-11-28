def obtener_calificacion_literal(calificacion):
    if 90 <= calificacion <= 100:
        return 'A'
    elif 80 <= calificacion <= 89:
        return 'B'
    elif 70 <= calificacion <= 79:
        return 'C'
    elif 60 <= calificacion <= 69:
        return 'D'
    else:
        return 'F'

def main():
    calificaciones = []
    
    # Recibe 10 calificaciones
    for i in range(10):
        try:
            calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
            calificaciones.append(calificacion)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            i -= 1  # Repetir la iteración si hay un error en la entrada.

    # Imprime las calificaciones con su calificación literal equivalente
    for i, calificacion in enumerate(calificaciones, start=1):
        calificacion_literal = obtener_calificacion_literal(calificacion)
        print(f"Calificación {i}: {calificacion} - Calificación Literal: {calificacion_literal}")

if __name__ == "__main__":
    main()
