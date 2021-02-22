def calculaImposto(sal,imposto = 20):
    imposto = imposto/100 # calcula a porcentagem do valor
    novoSalario = sal - (sal*imposto)

    return novoSalario

salario = float(input("Informe seu salário: "))
# desconto = float(input("Qual o valor da porcentagem de imposto: ")) 

print(f"Seu salário líquido é R${calculaImposto(salario)}")