from agregacao import Cliente, Conta

c1 = Cliente("Madruga","98 91234-5678","123.456.789-98","Rua das patativas 35, bairro ilhinha")


conta1 = Conta(1234,c1,1100,2000)

print(f"\n{conta1.titular.nome} possui R$ {conta1.saldo} e mora no endereço {conta1.titular.endereco} e possui telefone {conta1.titular.telefone} e um limite de R$ {conta1.limite}\n")
