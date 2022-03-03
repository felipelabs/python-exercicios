# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contaDigitos(numero):
  tamanho = len(str(numero))
  return tamanho

numero = int(input("Informe um número: "))
print(f"A quantidade de dígitos do número {numero} é: {contaDigitos(numero)}.")
