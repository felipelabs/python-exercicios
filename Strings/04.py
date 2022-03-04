'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
'''

def nome():
  name = input("Informe o seu nome:")
  return name

def  mostraNome():
  name = nome()
  tamanho = len(name)
  cont = 0
  fullName = ""
  while cont < tamanho:
    if cont == 0:
      print(name[cont])
      fullName += name[cont]
      cont += 1
    else:
      fullName += name[cont] 
      print(fullName)
      cont += 1

mostraNome()