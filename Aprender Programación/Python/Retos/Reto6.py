maximo_intentos = 3
intentos = 0
acierto = False
numero = range(10, 21)
while intentos < maximo_intentos and not acierto:
    usuario = int(input("Ingrese un numero: "))
    
    if usuario in numero:  
        acierto = True
        print("Numero válido")
    else:
        intentos+=1
        print("Esta fuera del rango [10, 20]")
        print(f"Te quedan {maximo_intentos-intentos} intentos")
if not acierto:
    print("Intentos agotados")