# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

import os
import random

listOne = []
listTwo = []
listThree = []
cont = 0

for i in range(10):
  listOne.append(random.randrange(10, 50))
  listTwo.append(random.randrange(10, 50))

for i in range(10):
  listThree.append(listOne[i])
  for j in range(1):
    listThree.append(listTwo[cont])
    cont += 1

os.system('cls')
print(f"Lista 01:\n {listOne}")
print(f"Lista 02:\n {listTwo}")
print(f"Lista (valores intercalados):\n {listThree}")
