print("="*10,"ATIVIDADE 2","="*10)

sal = float(input("Informe seu salário no dia: "))
horas = float(input("Quantas horas você trabalhou no dia? "))

horasTrabalhadas = sal / horas

print("Você receberá R$ {:.2f} por horas trabalhadas\n\n".format(horasTrabalhadas))