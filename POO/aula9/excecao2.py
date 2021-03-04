while True:
    try:
        salario = float(input("Informe seu salário: "))
    except Exception as erro:
        print(f"Informe um valor decimal correto, o erro foi {erro.__class__}")
    else:
        break

print(f"Seu salário é: R${salario}")