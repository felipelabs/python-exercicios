# Faça um programa que leia 5 números e informe o maior número.

numero = [0, 0, 0, 0, 0]

for i in range(5):
  numero[i] = float(input("informe um numero:"))
print(max(numero))