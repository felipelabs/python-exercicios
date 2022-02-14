''' Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que 
a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''
import os
os.system("cls")

print("\tLoja de Tintas")

metrosQuadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = metrosQuadrados / 3
precoLitro = 80.0
capacidadeLitro = 18

latas = litros / capacidadeLitro
precoTotal = latas * precoLitro

print(f"Você precisará de: {latas} latas de tintas.")
print(f"Você pagará: R${precoTotal}.")