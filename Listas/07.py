# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

numeros = []
soma = []
multiplicacao = []
numero = 1

for i in range(5):
  numeros.append(int(input("Digite o {numeros}° número: ")))
  soma += numeros
  multiplicacao *= numeros
  numero += 1

print(f"Números: {numeros}")
print(f"\nSoma: {soma}")
print(f"Multiplicação: {multiplicacao}")
