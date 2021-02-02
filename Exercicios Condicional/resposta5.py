vPermitida = float(input("Qual a velocidade permitida? "))
vMotorista = float(input("Qual a velocidade do motorista? "))

# calculando 20% a mais
vPermitida20 = (vPermitida * 0.2) + vPermitida

#calculando 50% a mais
vPermitida50 = (vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("Tudo certo, não precisa pagar multa")
elif vMotorista > vPermitida and vMotorista <= vPermitida20:
    print("Você cometeu infração média\nAssim irá pagar uma multa de R$ 85,00 e receber 4 pontos na carteira\n\n")
elif vMotorista > vPermitida20 and vMotorista <= vPermitida50:
    print("Você cometeu infração grave\nAssim irá pagar uma multa de R$ 127,00 e receber 5 pontos na carteira")
elif vMotorista > vPermitida50:
    print("Você cometeu infração gravíssima\nAssim irá pagar uma multa de R$ 574,00 além de receber 7 pontos na carteira\nTer a carteira apreendida e\nTer o direito de dirigir suspenso")
