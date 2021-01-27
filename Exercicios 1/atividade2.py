print("*"*10,"ATIVIDADE 2","*"*10)

sal = float(input("Informe seu salário: "))
horas = int(input("Quantas horas você trabalha por dia? "))

horaTrabalhada = sal / horas
print("Você receberá {:.2f} por hora trabalhada\n".format(horaTrabalhada))