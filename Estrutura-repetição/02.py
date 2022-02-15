''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''

usuario = input("Informe um usuário:")
senha = input("Informe uma senha:")

while usuario == senha:
  print("A senha não pode ser igual ao usuário.")
  senha = input("Informe uma senha:")
else:
  print(f"Cadastro feito, seu usuário é {usuario} e sua senha é {senha}.")