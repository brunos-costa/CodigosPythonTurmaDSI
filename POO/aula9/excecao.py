num1 = int(input("Informe um valor numérico: "))
num2 = int(input("Informe outro valor numérico: "))

try:
    resultado = num1 / num2
except Exception as erro:
    print(f"Houve o erro: {erro.__class__}")
else:
    print(f"O resultado é {resultado}")