# Reglas (léelas con calma)
# El usuario debe ingresar un número par
# Tiene máximo 3 intentos
# Si ingresa un número par → imprimir "Correcto" y terminar
# Si falla 3 veces → imprimir "Intentos agotados"
# ❌ No usar for
# ❌ No usar funciones
# ✅ Usar while, if, input

# intentos = 0
# max_intentos = 3

# while intentos < max_intentos:
#     numero = int(input("Digita un numero: "))

#     if numero % 2 == 0:
#         print("Correcto")
#         break
#     else:
#         intentos += 1
#         print("Error, vuelve a intentarlo")
#         print(f"Te quedan {max_intentos - intentos} intentos")
# if intentos == max_intentos:
#     print("Intentos agotados")
# --------------------------------------------------------------

# Bucle For
# Reglas:
# Contraseña correcta: "admin2026"
# Máximo 3 intentos
# Si acierta → "Acceso concedido" y termina
# Si falla los 3 → "Sistema bloqueado"
# Usar for
# La función solo devuelve True o False
# NO usar while
# NO usar break (sí, esto es intencional)

def validar(contraseña):
    return contraseña == "admin2026"

intentos = 0
acierto = False

for intentos in range(3):
    usuario = input("Digite su contraseña: ")
    acceso = validar(usuario)
    
    if acceso:
        acierto=True
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta. Intenta nuevamente")
        intentos+=1
        print(f"Te quedan #{maximo_intentos-intentos} intentos")
if not acierto:
    print("Sistema bloqueado.")
    