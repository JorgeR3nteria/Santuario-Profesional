# contador = 0

# for i in range(5):
#     usuario = int(input("Ingrese un numero: "))
#     if usuario > 10:
#         contador+=1
#     else:
#         print("Numero fuera del rango.")
# print (f"El total de numeros mayores fueron: {contador}")

#----------------------------------------------------------

#Pide 5 números
# Suma solo los números mayores a 10. Al final imprime la suma total.
# Reglas:
# Usa for
# Usa un acumulador
# No imprimas dentro del bucle (solo al final)
# mayores = 0
# for n in range(5):
#     user = int(input("Digita un numero: "))
#     if user > 10:
#         mayores+=user
#     else:
#         print("Numero por debajo del rango permitido [+10]")
# print(f"La suma total es: {mayores}")

# -----------------------------------------------------------

# Pide 5 números
# Cuenta:
# Cuántos son pares
# Cuántos son impares
# Cuántos son mayores a 10
# Cuántos son pares y mayores a 10
# Reglas:
# Usa solo for, if y contadores.

par=0
impar=0
mayores=0
par_y_mayor = 0

for n in range(5):
    user = int(input("Digita un numero: "))

    if user > 10:
        mayores+=1
        
    if user %2 ==0:
        par+=1
        if user > 10:
            par_y_mayor += 1
    else:
        impar+=1
print(f"El total de numeros pares fueron: {par}")
print(f"El total de numeros impares fueron: {impar}")
print(f"El total de mayores a 10 fueron: {mayores}")
print(f"El total de numeros pares es: {par} y los numeros mayores a 10 es: {mayores}")