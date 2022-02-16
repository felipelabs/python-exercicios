# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
media = []
contAprovados = 1
aluno = 1

for i in range(1, 11):
  soma = 0
  for j in range(1, 5):
    nota = int(input(f"Informe a {aluno}° do aluno:"))
    notas.append(nota)
    soma += nota
  aluno += 1
  media.append(soma/4)

for i in range(10):
  if media[i] >= 7:
    contAprovados += 1

print(f"Medias: {media}")
print(f"Possui {contAprovados} alunos Aprovados.")