# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

listaTemperatura = []

mes = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

mediaAnual = 0

for i in range(12):
  listaTemperatura.append(float(input(f"Digite a temperatura do mês de {mes[i]}:")))
  mediaAnual += listaTemperatura[i]

mediaAnual = mediaAnual / 12

print(f"Media Anual: {mediaAnual}")

for i in range(12):
  if listaTemperatura > mediaAnual:
    print(f"Temperatura: {listaTemperatura[i]}\nMês: {i} - {mes[i]}")