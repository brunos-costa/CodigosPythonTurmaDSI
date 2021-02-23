def verificaLetra(texto, letra):
    return texto.count(letra)


texto = str(input("Informe um texto qualquer: ")).lower()
letra = str(input("Informe uma letra qualquer: ")).lower()

print(f"A letra {letra} aparece {verificaLetra(texto,letra)}x no texto\n\n")