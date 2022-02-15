''' Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.'''


from prometheus_client import Counter


count = 1

while count == 1:
  paisA = float(input("Digite a pupulação do pais A:"))
  populacaoA = float(input("Informe a taxa de crescimento:"))
  paisB = float(input("Digite a pupulação do pais B:"))
  populacaoB = float(input("Informe a taxa de crescimento:"))
  
  counter = 0

  if paisA < paisB:
    while paisA < paisB and populacaoA <= populacaoB:
      populacaoA = float(input("Informe a taxa de crescimento:"))
    
    while paisA <= paisB:
      paisA += paisA * (populacaoA/100)
      paisB += paisB * (populacaoB/100)
      counter += 1
    
    print(f"Será necessários {counter} anos para a população do país A {paisA:0.0f} ultrapassar a do  país B {paisB:0.0f}.")

  else:
    while paisB < paisA and populacaoB <= populacaoA:
      populacaoB = float(input("Informe a taxa de crescimento:"))
    
    while paisB <= paisA:
      paisA += paisA * (populacaoA/100)
      paisB += paisB * (populacaoB/100)
      counter += 1
    
    print(f"Será necessários {counter} anos para a população do país B {paisB:0.0f} ultrapassar a do  país A {paisA:0.0f}.")
  
  count = int(input("Deseja repetir? \n[1] - Sim [2] - Não :"))
  if count == 1:
    paisA = 0
  else:
    count = 2

    