# Reglas:
# El usuario ingresa números
# Cuenta cuántos números son mayores que 10
# Termina cuando el usuario ingresa -1
# Al final imprime el total
# 👉 Escribe el código completo

# usuario=int(input("Digita un numero: "))
# contador = 0

# while usuario != -1:
#     if usuario >= 10:
#         contador += usuario
#         usuario=int(input("Digita un numero: "))
#         break
# print("Programa finalizado")

# Versión corregida
usuario = int(input("Digita un numero: "))
contador = 0

while usuario != -1:
    if usuario > 10:
        contador += 1
    usuario = int(input("Digita un numero: "))

print("Cantidad de numeros mayores a 10:", contador)
