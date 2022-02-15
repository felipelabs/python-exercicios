# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

numero = input("Informe um número: ")
ultimoNumero = 0
penultimoNumero = 0

if numero == 1:
  print('1')
elif numero == 2:
  print('1\n1')
else:
  count = 3
  print('1')
  print('1')
  while count <= numero:
    termo = ultimoNumero + penultimoNumero
    penultimoNumero = ultimoNumero
    ultimoNumero = termo
    count += 1
    print(termo)