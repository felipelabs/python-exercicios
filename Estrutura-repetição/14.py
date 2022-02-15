'''Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.'''

numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 1
par = 0
impar = 0

for numero in range(10):
  numeros[numero] = int(input(f"Informe o {count}° número:"))
  count += 1

for numero in range(10):
  if numeros[numero] % 2 == 1:
    par += 1
  else:
    impar += 1

print(f"Existe {par} números pares e {impar} numeros impares.")