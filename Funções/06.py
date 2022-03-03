# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def converter_hour(hour, minute):
  if hour > 12 and hour != 24:
    count = 0
    for i in range(hour):
      if i >= 12:
        count += 1
    return count
  elif hour == 24:
    return 0
  else:
    return hour


def message(hour, minute):
  print(f"Conversão: {converter_hour(hour, minute)}:{minute}.")

retry = 1
while retry == 1:
  print("\tConversor de Horas")
  hour = int(input("Digite a hora para conversão:"))
  minute = int(input("Digite os minutos:"))
  A = 'A.M'
  P = 'P.M'
  message(hour, minute)
  retry = int(input("Deseja realizar mais conversão? \n[1] - Sim \n[2] - Não"))