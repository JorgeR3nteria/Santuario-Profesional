# Reglas (léelas con calma)
# El usuario debe ingresar un número par
# Tiene máximo 3 intentos
# Si ingresa un número par → imprimir "Correcto" y terminar
# Si falla 3 veces → imprimir "Intentos agotados"
# ❌ No usar for
# ❌ No usar funciones
# ✅ Usar while, if, input

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    numero = int(input("Digita un numero: "))

    if numero % 2 == 0:
        print("Correcto")
        break
    else:
        intentos += 1
        print("Error, vuelve a intentarlo")
        print(f"Te quedan {max_intentos - intentos} intentos")
if intentos == max_intentos:
    print("Intentos agotados")
