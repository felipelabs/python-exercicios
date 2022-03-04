'''Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
F
U
L
A
N
O
'''

def nome():
  name = input("Informe o seu nome:")
  return name

def  mostraNome():
  name = nome()
  print("\n".join(name))

mostraNome()