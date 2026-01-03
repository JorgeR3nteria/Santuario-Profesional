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