'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F
'''

def nome():
  name = input("Informe o seu nome:")
  return name

def  mostraNomeVertical():
  name = nome()
  tamanho = len(name)
  cont = 0
  nomeReduzido = " ".join(name)
  nomeReduzido = nomeReduzido.split(' ')

  while tamanho > cont:
    if cont == 0:
      print(name)
    else:
      nomeReduzido.pop()
      print("".join(nomeReduzido))
    cont += 1
  
mostraNomeVertical()