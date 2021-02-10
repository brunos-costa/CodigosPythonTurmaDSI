produtos = [
    "Pão 1kg", 9.00,
    "Leite",5.59,
    "Café",3.99,
    "Açúcar",2.25,
    "Azeite", 16.99,
    "Arroz 5kg",19
]

print("-"*40)
print(f"{'Lista de Compras':^40}")
print("-"*40)
for indice,itens in enumerate(produtos):
    if indice%2==0:
        print(f"{itens:.<30}R$",end="")
    else:
        print(f"{itens:>8}")

print("-"*40)
