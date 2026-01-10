# El programa debe pedir exactamente 5 números
# 2️⃣ Debe contar:
# cuántos números son pares
# cuántos son impares
# cuántos son mayores a 10
# cuántos son pares y mayores a 10
# 3️⃣ Al final, mostrar solo un resumen, no imprimir durante el bucle
# 4️⃣ No usar listas
# 5️⃣ No usar funciones (solo lógica directa)

impares=0
par=0
mayores=0
par_mayor=0

for n in range(5):
    user = int(input("Digita un numero: "))
    
    if user %2 ==0:
        par+=1
        if user > 10:
            par_mayor+=1
            
    else:
        impares+=1
    if user > 10:
        mayores+=1
print(f"Tus numeros pares fueron: {par}")
print(f"Tus numeros impares fueron: {impares}")
print(f"Tus numeros pares y mayores fueron: {par_mayor}")
print(f"Los numeros mayores fueron: {mayores}")