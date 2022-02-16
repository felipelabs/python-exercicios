# Faça um Programa que leia 4 notas, mostre as notas e a média na tela

lista = []
cont = 0
media = 0

for i in range(1, 5):
  lista.append(float(input(f"Informe a {cont}° nota:")))
  media += lista[i]
  cont += 1

cont = 1
for i in range(4):
  print(f"Nota {cont} : {lista[i]}")
  cont += 1

media = media / 4
print(f"A media das notas é : {media}")