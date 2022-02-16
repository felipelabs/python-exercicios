# Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
consoantes = 0

for i in range(10):
  vetor.append(input("Informe uma letra:"))
  const = vetor[i]
  if const not in ('a', 'e', 'i', 'o', 'u'):
    consoantes += 1

print(f"Foram lidas: {consoantes} consoantes.")