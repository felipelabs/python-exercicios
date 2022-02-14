# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produtoUm = float(input('Informe o preço do primeiro produto: '))
produtoDois = float(input('Informe o preço do segundo produto: '))
produtoTres = float(input('Informe o preço do terceiro produto: '))

if produtoUm < produtoDois and produtoUm < produtoTres:
    print(f"Você deve comprar o produto um:{produtoUm} ")
elif produtoDois < produtoUm and produtoDois < produtoTres:
    print(f"Você deve comprar o produto dois:{produtoDois} ")
else:
    print(f"Você deve comprar o produto três: {produtoTres}")