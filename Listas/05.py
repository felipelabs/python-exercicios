# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

vetor = []
vetorPar = []
vetorImpar = []
cont = 1

for i in range(1, 21):
  vetor.append(int(input("Digite o {cont}° numero: ")))
  cont += 1

for i in range(1, 21):
  if vetor[i] % 2 == 0:
    vetorPar.append(vetor[i])
  else:
    vetorImpar.append(vetor[i])

print(f'Vetor : {vetor}')
print(f'Vetor par: {vetorPar}')
print(f'Vetor Impar: {vetorImpar}')
