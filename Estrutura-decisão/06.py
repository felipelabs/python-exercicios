# Faça um Programa que leia três números e mostre o maior deles.

primeiroNumero = float(input('Digite o primeiro número: '))
segundoNumero = float(input('Digite o segundo número: '))
terceiroNumero = float(input('Digite o terceiro número: '))

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    print(f"O maior número é o :{primeiroNumero} ")
elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    print(f"O maior número é o :{segundoNumero} ")
else:
    print(f"O maior número é o : {terceiroNumero}")