def es_par(numero):
    return numero %2 == 0
intentos = 0
maximo_intentos = 3
acierto = False

while intentos < maximo_intentos and not acierto:
    usuario = int(input("Ingresa un numero: "))
    validar = es_par(usuario)
    
    if validar:
        acierto=True
        print("Correcto")
    else:
        intentos+=1
        print("Intenta nuevamente")
        print(f"Te quedan #{maximo_intentos - intentos} intentos")
if not acierto:
    print("Intentos agotados.")