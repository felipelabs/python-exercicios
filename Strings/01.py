'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
'''

def informaString():
  string = input("Informe a string:")
  return string

def imprimeString(string, numero):
  print(f"String,  {numero} : {string}")

def lenString(string):
  print(f"Tamanho de {string} : {len(string)}, caracteres.")

string1 = informaString()
string2 = informaString()

imprimeString(string1, 1)
imprimeString(string2, 2)

lenString(string1)
lenString(string2)

if len(string1) == len(string2):
  print("Possuem o mesmo tamanho.")
else:
  print("Possuem tamanhos diferentes.")

if string1 == string2:
  print('Possuem o mesmo valores.')
else:
  print('Possui valores diferentes.')