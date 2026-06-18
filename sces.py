produtos = [
    [111, "Chave", 300, "A-190"] ##produto já existente dentro do sistema, para poupar uso repetitivo do código
]

def adicionar_produto(): ##essa função adicionará os produtos desejados pelo usuário dentro do sistema de estoque
    global IDproduto
    global NomeProduto
    IDproduto = int(input("Qual o ID do produto?: "))
    NomeProduto = input("Qual o nome do produto?: ")
    quantidadeProduto = int(input("Qual a quantidade em estoque do produto?: "))
    localizaçãoProduto = input("Qual a localização do produto?: ")
    produtos.append([IDproduto, NomeProduto, quantidadeProduto, localizaçãoProduto])
    travar_menu()

def travar_menu():
    input("\nPressione <ENTER> para continuar...")
    

def listagem_produtos(): ##função responsável por listar os produtos 5existentes no sistema de estoque
    for linha in produtos:
            print(linha)
    travar_menu()

def buscar_produto(): ##essa função busca os produtos dentro da matriz
    IDProcurado = int(input("Qual o ID do produto procurado?: "))
    produtoEncontrado = -1
    for linha in produtos:
        if IDProcurado == linha[0]:
            print(f"Produto encontrado! {linha}")
            produtoEncontrado = 1
            break

    if produtoEncontrado == -1:
        print("Esse produto não existe! Digite um ID existente.")
    travar_menu()

def atualizar_estoque(): ##essa função modificará a quantidade de um produto
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
        print("Quantidade atualizada!")
    travar_menu()

def estoque_minimo():
    for linha in produtos:
        if linha[2] < 5:
            print(f"Alerta! {linha} está com baixa quantidade: {linha[2]}")
            break

    else:
        print("Tudo certo! Prossiga com o sistema.")
    travar_menu()


while True: ##esse loop roda para sempre!
    print("\n🏭 Bem vindo ao menu interativo Sistema de Controle de Estoque Simplificado (SCES)! \nOs produtos serão organizados em: ID, Nome do produto, Quantidade e Localização (X- número). \nPor favor selecione uma opção:")
    print("\n1- Adicionar produto | 2 - Listar produtos | 3- Buscar produto | 4- Atualizar estoque | 5- Verificar estoque mínimo | 6- Sair\n")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        adicionar_produto()
    elif (opcao == "2"):
        listagem_produtos()
    elif (opcao == "3"):
        buscar_produto()
    elif (opcao == "4"):
        atualizar_estoque()
    elif (opcao == "5"):
        estoque_minimo()
    elif (opcao == "6"):
        print("Sessão encerrada. Saindo...")
        break

