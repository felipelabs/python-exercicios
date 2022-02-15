'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.'''

ultimoNumero = 0
penultimoNumero = 0
termo = 0
count = 1

while termo <= 500:
  termo = ultimoNumero + penultimoNumero
  penultimoNumero = ultimoNumero
  ultimoNumero = termo
  count += 1
  print(termo)