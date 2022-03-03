# Reverso do número.
# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def numberReverse(number):
  reverseNumber = list(reversed(number))
  return reverseNumber

number = int(input("Informe um número: "))
print(f"O inverso do número {number} é: {numberReverse(number)}")

