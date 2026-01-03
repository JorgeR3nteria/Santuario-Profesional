# Reglas:
# Pide números al usuario
# Mientras el número sea distinto de 0:
# Si es par → imprime "Par"
# Si es impar → imprime "Impar"
# Cuando el usuario escriba 0 → termina
# ✋ No uses funciones todavía
# 👉 Escribe el código completo

numero= int(input("Digita un numero: "))

while numero !=0:
    if numero %2 == 0:
        print("Numero par")
        numero = int(input("Digita un numero: "))
    else:
        print("Numero impar")
        numero = int(input("Digita un numero: "))
print("Programa finalizado")