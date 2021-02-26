from pymongo import MongoClient
# estabelecendo a conexão
cliente = MongoClient('localhost',27017)

banco = cliente.santander# criando um banco

colecao = banco.clientes# criando collections

while True:
    print(f"{' MENU ':=^40}")
    op = int(input('''
        1. Inserir dados
        2. Exibir dados
        3. Excluir dados
        4. Sair

        Qual sua escolha: '''))
    if op == 1:
        cpf = int(input("Informe o seu cpf(somente números): "))
        nome = str(input("Informe o seu nome: ")).title()
        sexo = str(input("Informe o seu sexo: (m/f): ")).lower()
        sal = float(input("Informe o seu salário "))
        end = str(input("Informe o seu endereço: "))

        # inserindo dados na collection
        colecao.insert_one({
            'cpf':cpf,
            'nome':f'{nome}',
            'sexo':f'{sexo}',
            'salario':sal,
            'endereco':f'{end}'
        })
        print("\nDados inseridos com sucesso\n")

    elif op == 2:
        print(f"{' Exibindo os dados ':-^40}")
        for item in colecao.find():
            print(f"{item['nome']}, possui salário de R${item['salario']} e mora no endereço {item['endereco']} com cpf= {item['cpf']}")
        print("-"*40)
    elif op == 3:
        escolha = int(input("Qual o cpf do cliente que deseja excluir: "))
        resultado = colecao.delete_one({
            'cpf':escolha
        })
        print("Clientes excluídos: ",resultado.deleted_count)
        # contando quantos itens foram excluidos
        
    elif op == 4:
        break


