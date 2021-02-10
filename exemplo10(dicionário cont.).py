pessoas = {
    "nome":"Bruno",
    "idade":21,
    "bairro":"Turu"
    }

print(pessoas)

print(f"Olá {pessoas['nome']}, você tem {pessoas['idade']} anos e mora no bairro {pessoas['bairro']} \n\n")

# print(type(pessoas))

print(pessoas.keys())# exibindo as chaves
print(pessoas.values())# exibindo o conteúdo
print(pessoas.items())# exibindo o s itens (chave e valor)

# exibir as chaves
for chave, valor in pessoas.items():
    print(f"{chave.title()} = {valor}")# .title() - deixa 1ª letra em maiúsculo

print(f"O tamanho do dicionário é {len(pessoas)}")

# inserindo mais uma chave e valor
pessoas.update({'sexo':'m'})
print(pessoas)

print("\n\n")

# Prencher uma lista com dicionários

lista = []
for cont in range(0,2):
    pessoas["nome"] = input("Informe seu nome: ")
    pessoas["idade"] = int(input("Informe sua idade: "))
    pessoas["bairro"] = input("Informe seu bairro: ")
    pessoas["sexo"] = input("Informe seu sexo: ")

    lista.append(pessoas.copy())# copiando dicionário dentro de uma lista

print(lista)

print(lista[0]['nome'])# mostrando um item dentro da lista