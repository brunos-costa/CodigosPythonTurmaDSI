from datetime import date
anoAtual = date.today().year
def divisoria():
    print("-"*50)

nome = str(input("Informe seu nome: "))
divisoria()

idade = int(input("Informe sua idade: "))
divisoria()

print(f"Olá {nome} você nasceu no ano de : {anoAtual - idade}")
divisoria()