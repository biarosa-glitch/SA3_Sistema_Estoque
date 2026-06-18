produtos = [
    [123, "Chave", 300, "A-190"]
]

def adicionar_produto():
    global IDproduto
    global NomeProduto
    IDproduto = int(input("Qual o ID do produto?: "))
    NomeProduto = input("Qual o nome do produto?: ")
    quantidadeProduto = int(input("Qual a quantidade em estoque do produto?: "))
    localizaçãoProduto = input("Qual a localização do produto?: ")
    produtos.append([IDproduto, NomeProduto, quantidadeProduto, localizaçãoProduto])
    

def listagem_produtos():
    for linha in produtos:
        print(linha)

def buscar_produto():
    IDProcurado = int(input("Qual o ID do produto procurado?: "))
    produtoEncontrado = -1
    for linha in produtos:
        if IDProcurado == linha[0]:
            print(f"Produto encontrado! {linha}")
            produtoEncontrado = 1
        if produtoEncontrado == -1:
            print("Esse produto não existe! Digite um ID existente.")

def atualizar_estoque():
    ID_desejado= int(input("Qual o ID do produto que deseja alterar a quantidade?: "))
    linha_produto = -1
    for i in range(len(produtos)):
        if ID_desejado == produtos[i][0]:
            linha_produto = i
    if linha_produto == -1:
        print("Produto não encontrado! Tente novamente.")
    else:
        Alteracao_qte = int(input("Qual a nova quantidade?: "))
        produtos[linha_produto][2] = Alteracao_qte



adicionar_produto()
listagem_produtos()
buscar_produto()
atualizar_estoque()
listagem_produtos()