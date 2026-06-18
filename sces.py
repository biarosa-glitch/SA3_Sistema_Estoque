produtos = []

def adicionar_produto():
    IDproduto = int(input("Qual o ID do produto?: "))
    NomeProduto = input("Qual o nome do produto?: ")
    quantidadeProduto = int(input("Qual a quantidade em estoque do produto?: "))
    localizaçãoProduto = input("Qual a localização do produto?: ")
    produtos.append([IDproduto, NomeProduto, quantidadeProduto, localizaçãoProduto])
    

def listagem_produtos():
    for linha in produtos:
        print(linha)

def buscar_produto():
    print("")

def atualizar_estoque():
    print("")

adicionar_produto()
listagem_produtos()