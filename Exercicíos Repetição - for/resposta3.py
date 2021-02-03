import time
import os

totalPessoas = int(input("Serão dadas boas vindas para quantas pessoas?"))

# CONTADORES
homens = 0
mulheres = 0

for cont in range(1,totalPessoas+1):
    nome = input("Qual seu nome? ")
    sexo = input("Qual o seu sexo? m ou f: ")
    
    if sexo=="m":
        print(f"Bem vindo Sr. {nome}")
        homens +=1
    else:
        print(f"Bem vinda Sra. {nome}")
        mulheres +=1

    time.sleep(1)# espera 1 segundo
    os.system("cls")# limpa a tela do sistema

print(f"Houve um total de {homens} homens e {mulheres} mulheres")



    