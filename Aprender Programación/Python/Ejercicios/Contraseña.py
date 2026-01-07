#Reglas del ejercicio
# 1. La contraseña correcta es: "admin2025"
# 2. El usuario tiene máximo 3 intentos
# 3. Si la contraseña es correcta → mostrar "Acceso concedido" y terminar
# 4. Si falla 3 veces → mostrar "Sistema bloqueado"
# 5. NO usar for
# 6. NO imprimir dentro de la función
# 7. La función solo debe devolver True o False

def password (clave):
    return clave=="admin2025"
intentos = 0
clave = input("Ingrese su contraseña: ")

while not password(clave):
    intentos +=1
    
    if intentos == 3:
        print ("Sistema bloqueado")
        break
    print("Contraseña erronea, digitela nuevamente")
    clave = input("Ingrese su contraseña: ")

if password(clave):
    print("Acceso concedido")
    
# Otro ejercicio de contraseña
# Crea un programa que:
# Pida una contraseña
# Permita máximo 3 intentos
# Muestre en qué intento va
# Si acierta → “Acceso concedido”
# Si falla los 3 → “Acceso bloqueado”
# Restricciones (muy importantes)
# ❌ No usar break
# ❌ No usar exit()
# ✔️ Usar while
# ✔️ Usar una función validar()
# ✔️ Usar variables claras
# 💡 Esto simula sistemas reales (cajeros, plataformas, juzgados, etc.)

def validar (password):
    return password == "python2026"
intentos=0
max_intentos=3
acceso_concedido = False #Bandera

while intentos < max_intentos and not acceso_concedido:
    usuario = input("Ingrese su contraseña: ")
    acceso = validar(usuario)
    
    if acceso:
        print("Acceso concedido")
        acceso_concedido = True
    else:
        print("Acceso bloqueado")
        intentos+=1
        print(f"Te quedan {max_intentos - intentos} intentos")
if not acceso_concedido:
    print("Vuelve a intentarlo mas tarde.")