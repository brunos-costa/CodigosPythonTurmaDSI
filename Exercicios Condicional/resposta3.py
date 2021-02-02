valor1 = float(input("Informe o valor do produto 1: "))
valor2 = float(input("Informe o valor do produto 2: "))
valor3 = float(input("Informe o valor do produto 3: "))

if valor1 <= valor2 and valor2 <= valor3:
    print("Compre o produto 1")
elif valor2 <= valor1 and valor1 <= valor3:
    print("Compre o produto 2")
elif valor3 <= valor2 and valor2 <= valor1:
    print("Compre o produto 3")

# PODE SER UTILIZADO A FUNÇÃO MIN()
# print("Dos 3 produtos o mais barato é {}".format(min(produto1, produto2, produto3)))