
print("Bem-Vindo Ao Python 🙋")
while True:
    nome = input ("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))
    
    if idade >= 18:
      print("Adulto")
    elif idade < 18 and idade >= 13:
     print("Adolescente")
    else:
      print("Criança")
      
      if idade == 0:
         break

for i in range(0, 10):
  print(i)
frutas = ["BANANA" , "KIWI" , "UVA", "MANGA", "===================="]
hardware = ["Processador" , "Placa Mãe" , "Placa de Video", "Fonte"]

for fr in frutas:
  print(fr)
for i in range(len(hardware)):
  print(hardware[i])  

  