# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import os
import random

listOne = []
listTwo = []
listThree = []
listFour = []
cont = 0
cont2 = 0

for i in range(10):
  listOne.append(random.randrange(10, 50))
  listTwo.append(random.randrange(10, 50))
  listThree.append(random.randrange(10, 50))

for i in range(10):
  listFour.append(listOne[i])
  for j in range(1):
    listFour.append(listTwo[cont])
    cont += 1
    for k in range(1):
      listFour.append(listThree[cont2])
      cont2 += 1

os.system('cls')
print(f"Lista 01:\n {listOne}")
print(f"Lista 02:\n {listTwo}")
print(f"Lista 03:\n {listThree}")
print(f"Lista 04(valores intercalados):\n {listFour}")
