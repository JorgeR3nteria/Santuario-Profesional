# Crea un programa que:
# Use un for con range y paso.
# Recorra los números del 1 al 50.
# Solo evalúe los múltiplos de 3.
# Cuente:
# cuántos son pares
# cuántos son impares
# Al final muestre:
# Total evaluados
# Pares
# Impares

Total = 0
pares = 0
impares = 0

for n in range(1, 51, 3):
    Total+=1
    if n %2 == 0:
        pares+=1
    else:
        impares+=1
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Total de numeros evaluados: {Total}")