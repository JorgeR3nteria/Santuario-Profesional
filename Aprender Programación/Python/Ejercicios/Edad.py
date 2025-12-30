def control_edad(edad):
    if edad <= 0:
        return "Edad invalida"
    if edad < 18:
        return "Eres menor de edad"
    return "Acceso permitido"
verificar = int(input("Ingrese su edad: "))
evaluar = control_edad(verificar)
print (evaluar)
