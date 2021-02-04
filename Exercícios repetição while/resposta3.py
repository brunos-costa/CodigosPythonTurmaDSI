cont = 1
soma = 0
contNegativos = 0

while cont <= 10:
    valor = int(input(f"Informe o {cont}º valor: "))

    if valor < 0:
        contNegativos += 1
    elif valor > 0:
        soma += valor
    
    cont += 1

print(f"A soma dos valores positivos é {soma}")
print(f"A quantidade  dos valores negativos é {contNegativos}")