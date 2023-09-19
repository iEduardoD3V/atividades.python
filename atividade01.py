produtos = ["Feijão", "Arroz", "Batata", "Cebola", "Tomate", "Suco", "Nutela", "Carne", "Frango", "Peixe"]

print ("Escolha uma Opção")


def adicionarProdutos():
    addProdutos = str(input("Nome do produto: \n"))
    produtos.append(addProdutos)
    print(produtos)
   

def removerProduto():
      removerProd = str(input("Digite nome do produto a ser removido: \n"))
      produtos.remove(removerProd)
      print(produtos)
 
            


def comprarProduto():
    quantidade = int(input("Quantidade de " + produtos[0] + " ? "))
    print(produtos[0], "\n"+"Quant:" , quantidade)
    produtos[0] = preco = 4.50
    print("Preço Unitario:", preco,"R$")
    precoTotal1 = preco*quantidade
    print("Preço Total:",precoTotal1,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[1] + "? "))
    print( produtos[1], "\n"+"Quant:" , quantidade)
    produtos[1] = preco = 3.90
    print("Preço Unitario:", preco,"R$")
    precoTotal2 = preco*quantidade
    print("Preço Total:",precoTotal2,"R$" + "\n" )


    quantidade = int(input("Quantidade de " + produtos[2] + "? "))
    print(produtos[2], "\n"+"Quant:" , quantidade)
    produtos[2] = preco = 3.0
    print("Preço Unitario:", preco,"R$")
    precoTotal3 = preco*quantidade
    print("Preço Total:",precoTotal3,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[3] + "? "))
    print(produtos[3], "\n"+"Quant:" , quantidade)
    produtos[3] = preco = 3.75
    print("Preço Unitario:", preco,"R$")
    precoTotal4 = preco*quantidade
    print("Preço Total:",precoTotal4,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[4] + "? "))
    print(produtos[4], "\n"+"Quant:" , quantidade)
    produtos[4] = preco = 4.35
    print("Preço Unitario:", preco,"R$")
    precoTotal5 = preco*quantidade
    print("Preço Total:",precoTotal5,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[5] + "? "))
    print(produtos[5], "\n"+"Quant:" , quantidade)
    produtos[5] = preco = 2.80
    print("Preço Unitario:", preco,"R$")
    precoTotal6 = preco*quantidade
    print("Preço Total:",precoTotal6,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[6] + "? "))
    print(produtos[6], "\n"+"Quant:" , quantidade)
    produtos[6] = preco = 24.99
    print("Preço Unitario:", preco,"R$")
    precoTotal7 = preco*quantidade
    print("Preço Total:",precoTotal7,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[7] + "? "))
    print(produtos[7], "\n"+"Quant:" , quantidade)
    produtos[7] = preco = 30
    print("Preço Unitario:", preco,"R$")
    precoTotal8 = preco*quantidade
    print("Preço Total:",precoTotal8,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[8] + "? "))
    print(produtos[8], "\n"+"Quant:" , quantidade)
    produtos[8] = preco = 12.20
    print("Preço Unitario:", preco,"R$")
    precoTotal9 = preco*quantidade
    print("Preço Total:",precoTotal9,"R$" + "\n" )

    quantidade = int(input("Quantidade de " + produtos[9] + "? "))
    print(produtos[9], "\n"+"Quant:" , quantidade)
    produtos[9] = preco = 22.35
    print("Preço Unitario:", preco,"R$")
    precoTotal10 = preco*quantidade
    print("Preço Total:",precoTotal10,"R$" + "\n" )


    total = precoTotal1 + precoTotal2 + precoTotal3 + precoTotal4 + precoTotal5 + precoTotal6 +precoTotal7 + precoTotal8 + precoTotal9 + precoTotal10
    print("Total:" , total,"R$\n")
    
  
while True:
    
  print("1-Adicionar Produto")
  print("2-Remover Produto")  
  print("3-Comprar")  
  print("4-Sair")
  escolha = input()
  if escolha == "1":
      adicionarProdutos()
  elif escolha == "2":
      removerProduto() 
  elif escolha == "3":
      comprarProduto()
  elif escolha == "4":
    break