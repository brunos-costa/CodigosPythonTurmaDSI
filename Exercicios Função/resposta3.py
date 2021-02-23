from random import randint

def sorteio(valor):
    aleatorio = randint(1,100)
    palpite = 1 # contador

    while valor != aleatorio:
        if valor > aleatorio:
            print("Informe um valor menor!!")
        elif valor < aleatorio:
            print("Informe um valor maior!!")
        palpite +=1
        valor = int(input("Informe um novo palpite: "))
    
    print(f"Parabéns você acertou o número com {palpite} palpites")

numero = int(input("Diga um palpite de um número entre 1 e 100: "))
sorteio(numero)