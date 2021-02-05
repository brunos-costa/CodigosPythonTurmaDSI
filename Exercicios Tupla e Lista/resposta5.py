from random import randint

aleatorio = list()

for cont in range(1,21):
    aleatorio.append(randint(1,900))

for cont in range(3,0,-1):
    print(f"Você tem {cont} chances para descobrir um dos valores da lista")

    op = int(input("Informe um valor: "))

    if op in aleatorio:
        print(F"{'PARABÉNS':*^40}")
        print("Você conseguiu encontrar o valor")

        break
    else:
        print("Eita, ainda não é esse valor, você consegue!!")
print(aleatorio)
