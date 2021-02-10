from os import system
from time import sleep

contato = {}
listaContato = []

while True:
    system("cls")

    print("="*40)
    print(f"{'Agenda':^40}")
    print("="*40)

    for itens in listaContato:
        for chave, valor in itens.items():
            print(f"{chave}:{valor}")

    print("1. Inserir um contato")
    print("2. Excluir um contato")
    print("3. Sair")
    op = int(input("Qual sua escolha? "))

    if op == 3:
        break
    elif op == 1:
        nome = str(input("Informe o nome do contato: ")).title()
        fone = int(input("Informe somente o número do contato(98xxxxxxxxx)"))

        contato[nome] = fone# a chave será o nome do contato e o valor será seu telefone
        listaContato.append(contato.copy())

        contato.clear()
    elif op == 2:
        print(listaContato)
        escolha = str(input("Informe o nome da pessoa que deseja excluir: ")).title()
        for itens in listaContato:
            if escolha in itens.keys():
                itens.pop(escolha)

print("="*40)


