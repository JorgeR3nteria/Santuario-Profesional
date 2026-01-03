# Reglas:
# Crea una función llamada es_par
# Recibe un número
# Devuelve True si es par, False si no
# Luego úsala para imprimir "Par" o "Impar"

def es_par(numero):
    if numero %2 ==0:
        return "Par"
    else:
        return "impar"
valor = es_par(numero = int(input("Digita un numero: ")))
resultado= valor
print(resultado)