# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
numero = 1
soma = 0

for i in range(10):
  vetor.append(int(input("Digite {numero}° número: ")))
  vetor[i] = vetor[i] ** 2
  soma += vetor[i]
  numero += 1

print(f"A soma do quadrado dos elementos é: {soma}")