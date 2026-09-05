#include <stdio.h>
#include <string.h>

#define MAX_PRODUTOS 100
#define ESTOQUE_MINIMO 5


/* Função dedicada a exibir o menu de opções do sistema de estoque e capturar a escolha do usuário. */
int menu () {
    int opcao;
    printf("===== SISTEMA DE ESTOQUE =====\n");
    printf("1. Cadastrar produto\n");
    printf("2. Listar produtos\n");
    printf("3. Buscar produto\n");
    printf("4. Entrada de estoque\n");
    printf("5. Saida de estoque\n");
    printf("6. Mostrar valor total do estoque\n");
    printf("7. Mostrar produto com maior quantidade\n");
    printf("8. Mostrar produto com menor quantidade\n");
    printf("9. Mostrar produto mais caro\n");
    printf("10. Listagem de produtos com estoque baixo\n");
    printf("0. Sair\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &opcao);
    getchar();
    return opcao;
}

/* Definição da estrutura Produto, que representa um produto no sistema de estoque, contendo nome, preço unitário e quantidade em estoque. */
typedef struct {
    char nome[50];
    float preco_unitario;
    int quantidade;
} Produto;

/* Função para cadastrar um novo produto no sistema de estoque, verificando se o limite máximo de produtos foi atingido e capturando os detalhes do produto. */
void cadastrar_produto(Produto *p, int *quantidade_produtos){

    /* Crio um ponteiro para o próximo produto a ser cadastrado, utilizando o endereço do array de produtos e o índice da quantidade atual de produtos. */
    if (*quantidade_produtos >= MAX_PRODUTOS) {
        printf("Limite de produtos atingido!\n");
        return;
    }

    Produto *novo_produto = &p[*quantidade_produtos];   

    printf("===== CADASTRAR PRODUTO =====\n");

    printf("Nome do produto: ");
    fgets(novo_produto->nome, sizeof(novo_produto->nome), stdin);

    printf("Preco unitario: ");
    scanf("%f", &novo_produto->preco_unitario);

    printf("Quantidade em estoque: ");
    scanf("%d", &novo_produto->quantidade);
    (*quantidade_produtos)++;
}

/* Função para listar todos os produtos cadastrados no sistema de estoque */
void listar_produtos(Produto *produtos, int quantidade_produtos) {

    printf("===== LISTA DE PRODUTOS =====\n");

    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }

    /* Loop para percorrer todos os produtos cadastrados e suas informações */
    for (int i = 0; i < quantidade_produtos; i++) {
        printf("Produto %d:\n", i + 1);
        printf("Nome: %s", produtos[i].nome);
        printf("Preco unitario: %.2f\n", produtos[i].preco_unitario);
        printf("Quantidade em estoque: %d\n", produtos[i].quantidade);
        printf("-----------------------------\n");
    }
}

/* Função para buscar um produto pelo nome no sistema de estoque */
void buscar_produto(Produto *produtos, int quantidade_produtos) {
    char nome_busca[50];
    printf("===== BUSCAR PRODUTO =====\n");
    printf("Digite o nome do produto: ");
    fgets(nome_busca, sizeof(nome_busca), stdin);

    /* Loop que percorre todos os nomes dos produtos cadastrados e compara com o nome buscado 
    A desvantagem é que ele não é case insensitive, ou seja, se o usuário digitar o nome do produto com letras maiúsculas ou minúsculas diferentes, a busca não funcionará corretamente. */
    for (int i = 0; i < quantidade_produtos; i++) {
        if (strcmp(produtos[i].nome, nome_busca) == 0) {
            printf("Produto encontrado:\n");
            printf("Nome: %s", produtos[i].nome);
            printf("Preco unitario: %.2f\n", produtos[i].preco_unitario);
            printf("Quantidade em estoque: %d\n", produtos[i].quantidade);
            return;
        }
    }
    printf("Produto nao encontrado.\n");
}

/* Função para registrar a entrada de estoque de um produto, permitindo ao usuário adicionar uma quantidade específica ao estoque existente. */
int entrada_estoque(Produto *produtos, int quantidade_produtos) {
    char nome_busca[50];
    printf("===== ENTRADA DE ESTOQUE =====\n");
    printf("Digite o nome do produto: ");
    fgets(nome_busca, sizeof(nome_busca), stdin);

    for (int i = 0; i < quantidade_produtos; i++) {
        if (strcmp(produtos[i].nome, nome_busca) == 0) {
            int quantidade_entrada;
            printf("Digite a quantidade a ser adicionada: ");
            scanf("%d", &quantidade_entrada);
            produtos[i].quantidade += quantidade_entrada;
            printf("Estoque atualizado. Nova quantidade: %d\n", produtos[i].quantidade);
            return 1;
        }
    }
    printf("Produto nao encontrado.\n");
    return 0; 
}

/* Função para registrar a saída de estoque de um produto, permitindo ao usuário remover uma quantidade específica do estoque existente, desde que haja quantidade suficiente. */
int saida_estoque(Produto *produtos, int quantidade_produtos) {
    char nome_busca[50];
    printf("===== SAIDA DE ESTOQUE =====\n");
    printf("Digite o nome do produto: ");
    fgets(nome_busca, sizeof(nome_busca), stdin);

    for (int i = 0; i < quantidade_produtos; i++) {
        if (strcmp(produtos[i].nome, nome_busca) == 0) {
            int quantidade_saida;
            printf("Digite a quantidade a ser removida: ");
            scanf("%d", &quantidade_saida);
            if (quantidade_saida <= produtos[i].quantidade) {
                produtos[i].quantidade -= quantidade_saida;
                printf("Estoque atualizado. Nova quantidade: %d\n", produtos[i].quantidade);
                return 1;
            } else {
                printf("Quantidade insuficiente em estoque.\n");
                return 0;
            }
        }
    }
    printf("Produto nao encontrado.\n");
    return 0; 
}

/* Função para calcular e exibir o valor total do estoque, somando o valor de cada produto com base em seu preço unitário e quantidade em estoque. */
void mostrar_valor_total_estoque(Produto *produtos, int quantidade_produtos) {
    printf("===== VALOR TOTAL DO ESTOQUE =====\n");
    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }
    float valor_total = 0.0;
    for (int i = 0; i < quantidade_produtos; i++) {
        float valor_produto = produtos[i].preco_unitario * produtos[i].quantidade;
        printf("Produto: %s - Valor em estoque: %.2f\n", produtos[i].nome, valor_produto);
        valor_total += valor_produto;
    }
    printf("Valor total do estoque: %.2f\n", valor_total);
}

/* Função para exibir o produto com a maior quantidade em estoque, percorrendo todos os produtos cadastrados e comparando suas quantidades. */
void mostrar_produto_maior_quantidade(Produto *produtos, int quantidade_produtos) {
    printf("===== PRODUTO COM MAIOR QUANTIDADE =====\n");
    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }

    int indice_maior = 0;
    for (int i = 1; i < quantidade_produtos; i++) {
        if (produtos[i].quantidade > produtos[indice_maior].quantidade) {
            indice_maior = i;
        }
    }
    printf("Nome: %s", produtos[indice_maior].nome);
    printf("Quantidade em estoque: %d\n", produtos[indice_maior].quantidade);
}

/* Função para exibir o produto com a menor quantidade em estoque, percorrendo todos os produtos cadastrados e comparando suas quantidades. */
void mostrar_produto_menor_quantidade(Produto *produtos, int quantidade_produtos) {
    printf("===== PRODUTO COM MENOR QUANTIDADE =====\n");
    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }

    int indice_menor = 0;
    for (int i = 1; i < quantidade_produtos; i++) {
        if (produtos[i].quantidade < produtos[indice_menor].quantidade) {
            indice_menor = i;
        }
    }
    printf("Nome: %s", produtos[indice_menor].nome);
    printf("Quantidade em estoque: %d\n", produtos[indice_menor].quantidade);
}

/* Função para exibir o produto mais caro, percorrendo todos os produtos cadastrados e comparando seus preços unitários. */
void mostrar_produto_mais_caro(Produto *produtos, int quantidade_produtos) {
    printf("===== PRODUTO MAIS CARO =====\n");
    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }

    int indice_mais_caro = 0;
    for (int i = 1; i < quantidade_produtos; i++) {
        if (produtos[i].preco_unitario > produtos[indice_mais_caro].preco_unitario) {
            indice_mais_caro = i;
        }
    }
    printf("Nome: %s", produtos[indice_mais_caro].nome);
    printf("Preco unitario: %.2f\n", produtos[indice_mais_caro].preco_unitario);
}

/* Função para listar produtos com estoque abaixo do mínimo definido, percorrendo todos os produtos cadastrados e verificando suas quantidades. */
void listar_produtos_estoque_baixo(Produto *produtos, int quantidade_produtos) {
    printf("===== PRODUTOS COM ESTOQUE BAIXO =====\n");
    if (quantidade_produtos == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }

    int encontrou = 0;
    for (int i = 0; i < quantidade_produtos; i++) {
        if (produtos[i].quantidade < ESTOQUE_MINIMO) {
            printf("Nome: %s", produtos[i].nome);
            printf("Quantidade em estoque: %d\n", produtos[i].quantidade);
            encontrou = 1;
        }
    }
    if (!encontrou) {
        printf("Nenhum produto com estoque baixo.\n");
    }
}

/* Função principal do programa, que inicializa o sistema de estoque, exibe o menu e processa as opções escolhidas pelo usuário em um loop até que ele decida sair. */
int main() {
    Produto produtos[MAX_PRODUTOS];
    int quantidade_produtos = 0;
    int opcao;
    do {
        opcao = menu();
        switch (opcao) {
            case 1:
                cadastrar_produto(produtos, &quantidade_produtos);
                break;
            case 2:
                listar_produtos(produtos, quantidade_produtos);
                break;
            case 3:
                buscar_produto(produtos, quantidade_produtos);
                break;
            case 4:
                entrada_estoque(produtos, quantidade_produtos);
                break;
            case 5:
                saida_estoque(produtos, quantidade_produtos);
                break;
            case 6:
                mostrar_valor_total_estoque(produtos, quantidade_produtos);
                break;
            case 7:
                mostrar_produto_maior_quantidade(produtos, quantidade_produtos);
                break;
            case 8:
                mostrar_produto_menor_quantidade(produtos, quantidade_produtos);
                break;
            case 9:
                mostrar_produto_mais_caro(produtos, quantidade_produtos);
                break;
            case 10:
                listar_produtos_estoque_baixo(produtos, quantidade_produtos);
                break;
            case 0:
                printf("Saindo do sistema...\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 0);
    return 0;
}

