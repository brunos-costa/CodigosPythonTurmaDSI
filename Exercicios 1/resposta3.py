print("+"*10,"ATIVIDADE 3","+"*10)
item1 = float(input("Informe o valor do item 1: "))
item2 = float(input("Informe o valor do item 2: "))
item3 = float(input("Informe o valor do item 3: "))

total = item1+item2+item3
print("O valor total da compra é R$ {}".format(total))
print("O  valor do desconto é R$ {}".format(total * 0.2))
print("Você irá pagar um total de R$ {}\n".format(total - (total*0.2)))