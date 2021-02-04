cont = 0
while True:
    valor = int(input("Informe um valor numérico qualquer: "))
    if valor == 0:
        break
    
    if cont == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    cont +=1



print(f"O maior valor é {maior} e o menor é {menor}\n\n")
