# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import os
import random

os.system('cls')

listaAltura = [
    1.33, 1.41, 1.65, 1.68, 1.82,
    1.12, 1.56, 1.65, 1.68, 1.84,
    1.64, 1.44, 1.65, 1.68, 1.86,
    1.31, 1.42, 1.65, 1.68, 1.88,
    1.32, 1.47, 1.65, 1.68, 1.81,
    1.33, 1.49, 1.65, 1.68, 1.83
]
listaIdade = []
mediaAltura = 0
cont = 0

for i in range(30):
  mediaAltura += listaAltura[i]
  listaIdade.append(random.randrange(6, 18))

mediaAltura = mediaAltura / 30

for i in range(30):
  if listaIdade[i] > 13:
    if listaAltura[i] < mediaAltura:
      cont += 1

print(f"Lista das Alturas:\n{listaAltura}")
print(f"Lista Idades:\n{listaIdade}")

print(f"Existem {cont} alunos com idade maior que 13 anos e altura menor que a media.")