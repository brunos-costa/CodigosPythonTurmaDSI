pessoas = ("Carlos","Mario","Luisa","Felipe")

print(type(pessoas))
print(pessoas)

# print(pessoas[1])

for itens in pessoas:
    print(itens)

print("Luisa está na posição ", pessoas.index("Luisa"))

for indice,itens in enumerate(pessoas):
    print(f"{indice:-<20}{itens}")
