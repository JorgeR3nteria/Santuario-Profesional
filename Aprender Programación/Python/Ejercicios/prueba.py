numeros = range(1, 21)
contador = 0
for i in numeros:
    if i %2 == 0:
        contador+=1
        print(i)
print(f"Total de números pares: {contador}")
