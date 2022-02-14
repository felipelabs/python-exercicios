'''Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = input("Informe seu sexo: [F]Feminino | [M]Masculino: ").upper()
h = float(input("Informe a sua altura: "))
pesoIdeal = 0

if sexo == "M":
    pesoIdeal = (72.7 * h) - 58
    pesoIdeal = round(pesoIdeal, 2)
elif sexo == "F":
    pesoIdeal = (62.1 * h) - 44.7
    pesoIdeal = round(pesoIdeal, 2)

print(f"Seu peso ideal é de: {pesoIdeal} Kg.")