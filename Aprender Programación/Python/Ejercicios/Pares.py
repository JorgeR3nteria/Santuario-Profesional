numero = int(input("Ingrese un número: "))
contador_pares = 0

while numero != 0:
    if numero % 2 == 0:
        contador_pares += 1
    numero = int(input("Ingrese otro número: "))

print("Cantidad de números pares:", contador_pares)
