import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

cod = int(input("Informe o código da disciplina: "))
nome = str(input("Qual o nome da disciplina: ")).lower()
descricao = str(input("Uma descrição para a disciplina: ")).lower()
ch = int(input("Qual a carga horária: "))

comando = "insert into disciplina values(%s,%s,%s,%s)"

valores = (cod,descricao,nome,ch)

consulta = conexao.cursor()

consulta.execute(comando,valores)

conexao.commit()# gravar os dados no banco

print(consulta.rowcount,"linha(s) inserida com sucesso!")
conexao.close()