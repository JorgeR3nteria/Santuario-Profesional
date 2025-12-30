def evaluar_saldo(saldo):
    if saldo < 0:
        return "Saldo inválido"
    if saldo < 100:
        return "Saldo insuficiente"
    return "Saldo suficiente"
valor = int(input("Digita un valor: "))
resultado = evaluar_saldo(valor)
print (resultado)