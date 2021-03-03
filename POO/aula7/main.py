from heranca2 import Aluno, Professor

a1 = Aluno("Matilda", 23, 987)

a1.mostraAluno()

print(f"A matricula de {a1.nome} é {a1.matricula}\n")

prof = Professor("Geraldo",54,3250.56)

prof.mostraProfessor()
print(f"O salário de {prof.nome} é R${prof.salario}")