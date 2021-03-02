from funcionario import Funcionario

f1 = Funcionario("Rosangela","Aux Administrativo",1600)

f1.relatorio()

f2 = Funcionario("Alberto","Pedreiro")

print(f"O salário de {f2.nome} é R$ {f2.sal}")
f2.nome = "Jorge"
print(f"O salário de {f2.nome} é R$ {f2.sal}")