# El usuario debe ingresar un número entre 1 y 10
# Reglas
# El usuario tiene máximo 3 intentos
# En cada intento:
# Si el número está entre 1 y 10 → imprimir "Número válido" y terminar
# Si no → imprimir "Número fuera de rango"
# Si falla los 3 intentos → imprimir "Intentos agotados"
# ❌ No usar for
# ❌ No usar funciones
# ✅ Usar while, if, input
# ✅ Usar comparaciones (<, >, <=, >=)
# ❌ No usar break (este es el reto extra)

# intentos = 0 
# max_intentos = 3

# while intentos < max_intentos:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero in range (1, 11):
#         print("Numero valido")
#     else:
#         print("Numero fuera de rango")
#         intentos+=1
#         print(f"Te quedan {max_intentos-intentos} intentos")
# print("Intentos agotados")

# Versión corregida
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    numero = int(input("Ingrese un numero: "))

    if numero >= 1 and numero <= 10:
        print("Numero valido")
        intentos = max_intentos  # fuerza la salida del while
    else:
        print("Numero fuera de rango")
        intentos += 1
        print(f"Te quedan {max_intentos - intentos} intentos")

if intentos == max_intentos:
    print("Intentos agotados")
