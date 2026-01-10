# El programa debe:
# Pedir 5 números al usuario
# Contar:
# cuántos son positivos
# cuántos son negativos
# cuántos son ceros
# Al final mostrar:
# total de números ingresados
# cantidad de positivos
# cantidad de negativos
# cantidad de ceros
# 📌 Reglas (importantes)
# Usa un solo for
# Usa contadores
# No uses listas
# El programa no debe romperse

positivos = 0
negativos = 0
ceros = 0
Total = 0

for n in range(5):
    numeros = int(input("Digite un numero: "))
    Total+=1
    
    if numeros > 0:
        positivos+=1
    elif numeros < 0:
        negativos+=1
    else:
        ceros+=1
print(f"Total de numeros ingresados: {Total}")
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")