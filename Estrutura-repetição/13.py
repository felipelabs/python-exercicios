''' Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''

from itertools import count


base = int(input("Informe a base:"))
expoente = int(input("Informe o expoente:"))
resultado = 1
count = 1

while count <= expoente:
  resultado *= base
  count += 1

print(f"\nResultado da {base} elevado a {expoente} = {resultado}")