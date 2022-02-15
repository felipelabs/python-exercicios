'''Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.'''

numeroUm = int(input("Informe o primeiro numero:"))
numeroDois = int(input("Informe o segundo numero:"))

if numeroUm > numeroDois:
  for i in range(numeroDois, numeroUm, 1):
    print(i)
elif numeroDois > numeroUm:
  for i in range(numeroUm, numeroDois, 1):
    print(i)
else:
  print("numeros iguais!!!")