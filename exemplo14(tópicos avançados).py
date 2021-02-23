lista = []
for cont in range(20):
    lista.append(cont)

print(lista)

# list comprehension
numeros = [cont**2 for cont in range(10)]
print(numeros)

# Utilizar lambda

soma = lambda x,y:x + y

print(soma(4,5))

dobro = list(map(lambda x:x*2,lista))

print(dobro)