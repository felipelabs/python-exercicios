# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Informe quanto você recebe por hora: "))

horasTrabalhadas = float(input("Informe as horas trabalhadas neste mês: "))

salario = valorHora * horasTrabalhadas

print(f"Seu salário neste mês é:{salario}.")