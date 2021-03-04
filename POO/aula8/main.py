from polimorfismo import Pessoa, Aluno, Professor

p1 = Pessoa("José")

p1.cpf = "12345678911"

print(len(p1.cpf))

p1.exibirDados()

aluno1 = Aluno("Joana", 123,"Desenvolvimento de sistemas")

aluno1.exibirDados()

prof = Professor("Ermenegildo",2000,44)

prof.exibirDados()
