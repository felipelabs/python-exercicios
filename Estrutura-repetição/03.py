'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd' '''


nome = input("Informe seu nome:")
idade = int(input("\nInforme sua idade:"))
salario = float(input("\nInforme seu salário:"))
sexo = input("Informe seu sexo 'f' ou 'm':").upper()
estadoCivil = input("Informe seu estado civil 's', 'c', 'v', 'd': ").upper()


while (len(nome) < 3) and (idade < 0 and idade >150) and (salario <= 0) and (sexo != 'F' and sexo != 'M') and (estadoCivil not in 'SCVD'):
  nome = input("Informe seu nome:")
  idade = int(input("\nInforme sua idade:"))
  salario = float(input("\nInforme seu salário:"))
  sexo = input("Informe seu sexo 'f' ou 'm':").upper()
  estadoCivil = input("Informe seu estado civil 's', 'c', 'v', 'd': ").upper()


print(f"Cadastro feito: \n nome: {nome} \n idade: {idade} \n salário: {salario} \n sexo: {sexo} \n Estado Civil: {estadoCivil} ")