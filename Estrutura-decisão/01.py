# Faça um Programa que peça dois números e imprima o maior deles.

numeroUm = int(input("Informe o primeiro número: "))
numeroDois = int(input("Informe o segundo número: "))

if numeroUm > numeroDois:
    print(f"O número {numeroUm} é o maior.")
elif numeroDois > numeroUm:
    print(f"O número {numeroDois} é o maior.")
else:
    print("Os números são iguais.")