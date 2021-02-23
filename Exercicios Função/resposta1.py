def somatorio(valor):
   soma = 0
   for cont in range(1,valor+1):
       soma +=cont
       if cont == valor:
           print(f"{cont}= {soma}")
       else:
            print(f"{cont}",end="+")
while True:
    numero = int(input("Informe um valor inteiro positivo: "))
    if numero > 0:
        somatorio(numero)
    else:
        print("Informe um valor positivo")
    
    op = str(input("Deseja continuar s/n: ")).lower()

    if op == "n":
        break
    


