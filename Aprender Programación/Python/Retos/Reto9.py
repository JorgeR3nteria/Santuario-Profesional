# Crea un programa en Python que:
# Pida 5 números enteros al usuario.
# Use un bucle for (obligatorio).
# Durante la ejecución:
# Cuente cuántos números son pares.
# Cuente cuántos números son impares.
# Cuente cuántos números son mayores a 10.
# Calcule la suma solo de los números impares.
# Al final, muestre todos los resultados.

pares = 0 
impares = 0
mayores = 0
suma_impares = 0

for n in range (5):
    numeros = int(input("Digita un numero: "))
    
    if numeros %2 == 0:
        pares+=1
    else:
        impares+=1
        suma_impares+=numeros
    if numeros > 10:
        mayores+=1
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Mayores a 10: {mayores}")
print(f"Suma de impares: {suma_impares}")