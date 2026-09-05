MAX_PRODUTOS = 100
ESTOQUE_MINIMO = 5

# Classe dedicada a salvar as informações essenciais de cada produto. O que vai diferenciar do paradigma orientado a objetos é que não vamos criar métodos dentro da classe, apenas atributos. A ideia é que a classe seja apenas um "molde" para os produtos, e as funções que manipulam esses produtos serão definidas fora da classe.
class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

# Função para exibir o menu principal do sistema de estoque, apresentando as opções disponíveis para o usuário e solicitando a escolha de uma opção.
def menu():
    print("===== SISTEMA DE ESTOQUE =====")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Entrada de estoque")
    print("5. Saída de estoque")
    print("6. Mostrar valor total do estoque")
    print("7. Mostrar produto com maior quantidade")
    print("8. Mostrar produto com menor quantidade")
    print("9. Mostrar produto mais caro")
    print("10. Listar produtos com estoque baixo")
    print("0. Sair")
    return int(input("Escolha uma opção: "))

# Função para cadastrar um novo produto, solicitando ao usuário as informações necessárias e adicionando o produto à lista de produtos, desde que o limite máximo de produtos não tenha sido atingido.
def cadastrar_produto(produtos):
    print("===== CADASTRO DE PRODUTO =====")

    if len(produtos) >= MAX_PRODUTOS:
        print("Limite de produtos atingido.")
        return

    nome = input("Digite o nome do produto: ")
    preco_unitario = float(input("Digite o preço unitário do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    produtos.append(Produto(nome, preco_unitario, quantidade))
    print("Produto cadastrado com sucesso.")

# Função para listar todos os produtos cadastrados, exibindo suas informações de forma organizada.
def listar_produtos(produtos):
    print("===== LISTA DE PRODUTOS =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for i, produto in enumerate(produtos):
        print(f"Produto {i + 1}:")
        print(f"Nome: {produto.nome}")
        print(f"Preço unitário: {produto.preco_unitario}")
        print(f"Quantidade em estoque: {produto.quantidade}")
        print("-----------------------------")

# Função para buscar um produto pelo nome, percorrendo a lista de produtos e exibindo suas informações caso seja encontrado.
def buscar_produto(produtos):
    print("===== BUSCAR PRODUTO =====")
    nome_busca = input("Digite o nome do produto a ser buscado: ")

    for produto in produtos:
        if produto.nome == nome_busca:
            print("Produto encontrado:")
            print(f"Nome: {produto.nome}")
            print(f"Preço unitário: {produto.preco_unitario}")
            print(f"Quantidade em estoque: {produto.quantidade}")
            return

    print("Produto não encontrado.")

# Função para registrar a entrada de estoque de um produto, solicitando ao usuário o nome do produto e a quantidade a ser adicionada.
def entrada_estoque(produtos):
    print("===== ENTRADA DE ESTOQUE =====")
    nome_busca = input("Digite o nome do produto para entrada de estoque: ")

    for produto in produtos:
        if produto.nome == nome_busca:
            quantidade_entrada = int(input("Digite a quantidade a ser adicionada: "))
            produto.quantidade += quantidade_entrada
            print(f"Entrada de estoque registrada. Nova quantidade em estoque: {produto.quantidade}")
            return

    print("Produto não encontrado.")

# Função para registrar a saída de estoque de um produto, solicitando ao usuário o nome do produto e a quantidade a ser removida.
def saida_estoque(produtos):
    print("===== SAÍDA DE ESTOQUE =====")
    nome_busca = input("Digite o nome do produto para saída de estoque: ")

    for produto in produtos:
        if produto.nome == nome_busca:
            quantidade_saida = int(input("Digite a quantidade a ser removida: "))
            if quantidade_saida > produto.quantidade:
                print("Quantidade insuficiente em estoque.")
                return
            produto.quantidade -= quantidade_saida
            print(f"Saída de estoque registrada. Nova quantidade em estoque: {produto.quantidade}")
            return

    print("Produto não encontrado.")

# Função para mostrar o valor total do estoque, calculando o valor de cada produto com base em seu preço unitário e quantidade em estoque, e exibindo o valor total acumulado.
def mostrar_valor_total_estoque(produtos):
    print("===== VALOR TOTAL DO ESTOQUE =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0
    for produto in produtos:
        valor_produto = produto.preco_unitario * produto.quantidade
        print(f"Produto: {produto.nome} - Valor em estoque: {valor_produto:.2f}")
        valor_total += valor_produto

    print(f"Valor total do estoque: {valor_total:.2f}")

# Função para mostrar o produto com a maior quantidade em estoque, percorrendo a lista de produtos e identificando aquele com a maior quantidade.
def mostrar_produto_maior_quantidade(produtos):
    print("===== PRODUTO COM MAIOR QUANTIDADE =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_maior = max(produtos, key=lambda p: p.quantidade)
    print(f"Nome: {produto_maior.nome}")
    print(f"Quantidade em estoque: {produto_maior.quantidade}")

# Função para mostrar o produto com a menor quantidade em estoque, percorrendo a lista de produtos e identificando aquele com a menor quantidade.
def mostrar_produto_menor_quantidade(produtos):
    print("===== PRODUTO COM MENOR QUANTIDADE =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_menor = min(produtos, key=lambda p: p.quantidade)
    print(f"Nome: {produto_menor.nome}")
    print(f"Quantidade em estoque: {produto_menor.quantidade}")

# Função para mostrar o produto mais caro, percorrendo a lista de produtos e identificando aquele com o maior preço unitário.
def mostrar_produto_mais_caro(produtos):
    print("===== PRODUTO MAIS CARO =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_caro = max(produtos, key=lambda p: p.preco_unitario)
    print(f"Nome: {produto_caro.nome}")
    print(f"Preço unitário: {produto_caro.preco_unitario}")

# Função para listar produtos com estoque abaixo do mínimo definido, percorrendo a lista de produtos e exibindo aqueles que possuem quantidade inferior ao limite estabelecido.
def listar_produtos_estoque_baixo(produtos):
    print(f"===== PRODUTOS COM ESTOQUE BAIXO =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produtos_estoque_baixo = [p for p in produtos if p.quantidade < ESTOQUE_MINIMO]

    if len(produtos_estoque_baixo) == 0:
        print("Nenhum produto com estoque abaixo do mínimo.")
        return

    for produto in produtos_estoque_baixo:
        print(f"Nome: {produto.nome}")
        print(f"Quantidade em estoque: {produto.quantidade}")
        print("-----------------------------")

# Função principal do programa, responsável por inicializar a lista de produtos, exibir o menu e processar as opções escolhidas pelo usuário.
def main():
    produtos = []
    opcao = -1

    while opcao != 0:
        opcao = menu()

        match opcao:
            case 1:
                cadastrar_produto(produtos)
            case 2:
                listar_produtos(produtos)
            case 3:
                buscar_produto(produtos)
            case 4:
                entrada_estoque(produtos)
            case 5:
                saida_estoque(produtos)
            case 6:
                mostrar_valor_total_estoque(produtos)
            case 7:
                mostrar_produto_maior_quantidade(produtos)
            case 8:
                mostrar_produto_menor_quantidade(produtos)
            case 9:
                mostrar_produto_mais_caro(produtos)
            case 10:
                listar_produtos_estoque_baixo(produtos)
            case 0:
                print("Saindo do sistema...")
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()