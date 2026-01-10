# numero = int(input("Ingrese un número: "))
# contador_pares = 0

# while numero != 0:
#     if numero % 2 == 0:
#         contador_pares += 1
#     numero = int(input("Ingrese otro número: "))

# print("Cantidad de números pares:", contador_pares)
#Ejercicio de pares e impares
# Pide 5 números
# cuántos son pares
# cuántos son impares
# Al final muestra ambos totales.
par = 0
impar = 0

for n in range (5):
    usuario = int(input("Digita un numero: "))
    if usuario %2 ==0:
        par+=1
    else:
        impar+=1
print(f"Tus numeros pares fueron: {par}")
print(f"Tus numeros impares fueron: {impar}")