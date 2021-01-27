print("*"*10,"ATIVIDADE 1","*"*10)

m2 = 850 # valor do m2 

base = float(input("Qual a largura(base) do terreno? "))
altura = float(input("Qual o comprimento(altura) do terro? "))

area = base * altura

custo = area * 850

print("Você irá pagar um total de R$ {:.3f} para construir uma casa \n\n".format(custo))
