'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.'''

numeroInt1 = int(input("Informe o 1º número inteiro: "))
numeroInt2 = int(input("Informe o 2º número inteiro: "))
numeroReal = float(input("Informe um número real: "))

# Cálculo1
operacao1 = (numeroInt1 * 2) * (numeroInt2 / 2)

# Cálculo2
operacao2 = (3 * numeroInt1) + numeroReal

# Cálculo3
operacao3 = (numeroReal ** 3)

print(f"O produto do dobro do primeiro com metade do segundo:{operacao1} ")
print(f"A soma do triplo do primeiro com o terceiro:{operacao2} ")
print(f"O terceiro elevado ao cubo:{operacao3} ")