pessoas = ["Fabio","Carlos","Regina","Vanusa"]

print(type(pessoas))

print(pessoas)

pessoas[1] = "Sergio"
# Adicionando elementos
pessoas.append("Sarah")# adiciona no final
pessoas.insert(2,"Flávio")# adiciona em qualquer lugar

for chave, valor in enumerate(pessoas):
    print(f"{chave:.<5}{valor}")

#removendo elementos
pessoas.pop()# remove o último elemento
pessoas.pop(1)
pessoas.remove("Flávio")

print(pessoas)

# copiando listas
pessoasBkp = pessoas[:]
pessoasBkp.append("Jerônimo")
print("\n\n",pessoas)
print(pessoasBkp,"\n\n")


pessoas.clear()# limpa a lista
# del(pessoas) -> excluir a variável lista
print(pessoas,"\n\n")
