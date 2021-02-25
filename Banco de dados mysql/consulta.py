import pymysql

# Estabelecer a conexão
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

consulta = conexao.cursor()# a função cursor é importante pois 
#permite interagir com o banco de dados

sql = "select * from disciplina"

consulta.execute(sql)

'''
 for itens in consulta:
     print(itens)
'''

# exibir a consulta personalizada
resultado = consulta.fetchall()

for itens in resultado:
    print(f"{itens[2]} com carga horária de {itens[3]}h")

conexao.close() # encerrando a conexão