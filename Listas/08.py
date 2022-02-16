# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

altura = []
idade = []
pessoa = 1

for i in range(1, 6):
  print(f"\n Pessoa n°{pessoa}")
  altura.append(float(input("\nInforme sua altura:")))
  idade.append(int(input("\nDigite sua idade: ")))
  pessoa += 1

altura.reverse()
idade.reverse()

print(f"Altura Invertida: {altura}")
print(f"Idade Inversa: {idade}")
