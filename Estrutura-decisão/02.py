# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = input("Informe um número: ")

if int(numero) < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é positivo")