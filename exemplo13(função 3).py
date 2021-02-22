def calculaImposto(sal, imposto = False):
    """
    Função que calcula o imposto de um funcionário
    \nsal: parâmetro que recebe o salário do funcionário
    \nimposto: parâmetro opcional que permite mudar o valor do imposto
    """
    if imposto:
        desconto = float(input("Qual a porcentagem do imposto: "))
    else:
        desconto = 20
    
    desconto = desconto/100
    return sal - (sal * desconto)

salario = float(input("Informe seu salário: "))


print(f"Seu salário com desconto é: R${calculaImposto(salario,True)}")