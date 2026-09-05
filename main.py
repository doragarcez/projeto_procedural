MAX_PRODUTOS = 100
ESTOQUE_MINIMO = 5


class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade


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


def mostrar_produto_maior_quantidade(produtos):
    print("===== PRODUTO COM MAIOR QUANTIDADE =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_maior = max(produtos, key=lambda p: p.quantidade)
    print(f"Nome: {produto_maior.nome}")
    print(f"Quantidade em estoque: {produto_maior.quantidade}")


def mostrar_produto_menor_quantidade(produtos):
    print("===== PRODUTO COM MENOR QUANTIDADE =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_menor = min(produtos, key=lambda p: p.quantidade)
    print(f"Nome: {produto_menor.nome}")
    print(f"Quantidade em estoque: {produto_menor.quantidade}")


def mostrar_produto_mais_caro(produtos):
    print("===== PRODUTO MAIS CARO =====")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    produto_caro = max(produtos, key=lambda p: p.preco_unitario)
    print(f"Nome: {produto_caro.nome}")
    print(f"Preço unitário: {produto_caro.preco_unitario}")


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