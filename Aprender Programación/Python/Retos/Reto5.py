# El usuario debe ingresar una contraseña
# Contraseña correcta: "python2025"
# Máximo 3 intentos
# Si acierta → "Acceso concedido"
# Si falla 3 veces → "Sistema bloqueado"
# La función SOLO devuelve True o False
# NO imprimir dentro de la función
# Qué debes entregar
# Una función
# Un while
# Un resultado final coherente

# Versión Omar
# contraseña = "python2024"
# max_intentos = 3
# intentos = 0

# def validar (contraseña_usuario):
#     return contraseña_usuario == contraseña
    
# while intentos < max_intentos:
#     user = input ("Ingrese su contraseña: ")
#     if validar(user):
#         print("Acceso Concedido")
#         break
#     else:
#         intentos +=1
#         if intentos == max_intentos:
#             print("Sistema bloqueado")    
# Otra versión
# intentos = 0
# max_intentos =3

# def validación (contraseña):
#     return contraseña=="Python2025"


# while intentos < max_intentos:
#     usuario = validación(input("Ingrese una contraseña: "))
#     intentos+=1
    
#     if not usuario and intentos<max_intentos:
#         print(f"Intento #{intentos}")
#     elif intentos == max_intentos:
#         print(f"Intento #{intentos}")
#         print("Acceso bloqueado")
#     else:
#         print("Acceso concedido")
#         break
#Mi versión 

def validar (contraseña): 
    return contraseña == "admin2026"

intentos = 0
max_intentos = 3
aciertos = False #Bandera

while intentos < max_intentos and not aciertos:
    usuario = input("Ingrese su contraseña: ")
    acceso = validar(usuario)
    
    if acceso:
        print("Acceso concedido")
        aciertos=True
    else:
        print("Contraseña incorrecta")
        intentos+=1
        print(f"te quedan {max_intentos - intentos} intentos")
if not aciertos:
    print("Sistema bloqueado")