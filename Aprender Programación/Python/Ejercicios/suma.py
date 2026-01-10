suma = 0

for numeros in range (5):
    usuario = int(input("Digita un numero: "))
    if usuario %2==0:
        suma+=usuario
print(f"El total es: {suma}")