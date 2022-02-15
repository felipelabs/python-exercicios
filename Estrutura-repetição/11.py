# Altere o programa anterior para mostrar no final a soma dos números.

numeroA= int(input("Informe o primeiro numero:"))
numeroB = int(input("Informe o segundo numero:"))
soma = 0

if numeroA > numeroB:
  for numeros in range(numeroA, numeroB, 1):
    soma += numeros
  print(f"A soma dos números é: {soma}.")
elif numeroB > numeroA:
  for numeros in range(numeroA, numeroB, 1):
    soma += numeros
  print(f"A soma dos números é: {soma}")
else:
  print("Números iguais.")