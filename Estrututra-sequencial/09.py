# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

f = input("Informe a temperatura em Fahrenheit: ")

c = 5 * ((float(f) - 32) / 9)

print(f"A temperatura é de {c} graus Celsius")