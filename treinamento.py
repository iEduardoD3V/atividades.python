nota1 = int(input("Digite Primeira Nota: "))
nota2 = int(input("Digite Segunda Nota "))
nota3 = int(input("Digite Terceira Nota "))
nota4 = int(input("Digite Quarta Nota "))

soma = nota1 + nota2 + nota3 + nota4
media = soma/4
print("Sua media é:", media)

if media >= 5:
  print("Aprovado🟢")
else:
  print("Reprovado🔴")