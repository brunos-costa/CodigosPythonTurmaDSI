print("*"*10,"ATIVIDADE 1","*"*10)

m2 = 850 #valor referente ao metro quadrado

base = float(input("Qual a largura (base) do terreno? "))
altura = float(input("Qual o comprimento (altura) do terreno? "))

area = base * altura

custo = area * m2
print("Você irá pagar um total de R$ {} para construir.\n\n".format(custo))
