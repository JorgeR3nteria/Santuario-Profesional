# Edad sin while
# def control_edad(edad):
#     if edad <= 0:
#         return "Edad invalida"
#     if edad < 18:
#         return "Eres menor de edad"
#     return "Acceso permitido"
# verificar = int(input("Ingrese su edad: "))
# evaluar = control_edad(verificar)
# print (evaluar)

#Edad con bucle while

def verificar_edad(edad):
    if edad <= 0:
        return "Edad inválida"
    if edad < 18:
        return "Menor de edad"
    return "Acceso permitido"

edad = int(input("Ingrese su edad: "))

while edad <= 0:
    print("Edad inválida. Intente nuevamente.")
    edad = int(input("Ingrese su edad: "))

resultado = verificar_edad(edad)
print(resultado)
