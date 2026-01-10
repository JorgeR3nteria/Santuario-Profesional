# El programa debe:
# Pedir 5 números
# Calcular:
# la suma de los positivos
# la suma de los negativos
# Mostrar:
# suma de positivos
# suma de negativos
# cuántos positivos hubo
# cuántos negativos hubo
# 📌 Reglas
# Un solo for
# Sin listas
# Usa contadores y acumuladores
# El 0 no suma a nada

positivos = 0
negativos = 0
sum_pos = 0
sum_neg = 0

for n in range(5):
    numeros = int(input("Digita un numero: "))
    
    if numeros < 0:
        negativos+=1
        sum_neg+=numeros
    elif numeros > 0:
        positivos+=1
        sum_pos+=numeros
print(f"Suma de positivos: {sum_pos}")
print(f"Suma de negativos: {sum_neg}")
print(f"Numeros positivos fueron: {positivos}")
print(f"Numeros negativos fueron: {negativos}")