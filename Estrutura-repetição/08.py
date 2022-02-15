# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros =[0, 0, 0, 0, 0]
soma = 0

for i in range(5):
  numeros[i] = float(input("Informe um numero:"))
  soma += numeros[i]

print(f'Soma: {soma}')
print(f'Média: {soma / 5}')