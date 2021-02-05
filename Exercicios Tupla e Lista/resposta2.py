valores = list()

for cont in range(1,11):
    valores.append(int(input(f"Informe o valor {cont}: ")))

print(valores)
for cont in valores:
    if cont % 2==0:
        valores.remove(cont)
print(f"Lista sem os valores pares: {valores}\n\n",)