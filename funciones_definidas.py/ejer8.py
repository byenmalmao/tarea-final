def contar_frutas(*frutas):
    conteo_frutas = {}
    for fruta in frutas:
        conteo_frutas[fruta] = conteo_frutas.get(fruta, 0) + 1
    return conteo_frutas


frutas_ingresadas = input("Ingrese las frutas: ").split()

conteo_frutas = contar_frutas(*frutas_ingresadas)

print("Cantidad de frutas encontradas:")
for fruta, cantidad in conteo_frutas.items():
    print(f"{fruta}: {cantidad}")
