class BST:
    def __init__(self, dado=None):  # Inicializa um nodo da árvore binária de busca
        self.dado = dado  # Armazena o dado do nodo
        self.esquerda = None  # Inicializa o ponteiro para o filho esquerdo como None
        self.direita = None  # Inicializa o ponteiro para o filho direito como None

    def inserir(self, dado):  # Insere um novo dado na árvore
        if self.dado is None:  # Se a árvore estiver vazia
            self.dado = dado  # Define o dado do nodo raiz
        else:
            if dado < self.dado:  # Se o dado a ser inserido for menor que o dado do nodo atual
                if self.esquerda:  # Se o filho esquerdo existir
                    self.esquerda.inserir(dado)  # Insere o dado na subárvore esquerda
                else:
                    self.esquerda = BST(dado)  # Cria um novo nodo à esquerda
            else:  # Se o dado a ser inserido for maior ou igual ao dado do nodo atual
                if self.direita:  # Se o filho direito existir
                    self.direita.inserir(dado)  # Insere o dado na subárvore direita
                else:
                    self.direita = BST(dado)  # Cria um novo nodo à direita

    def folhas(self, lst):  # Define a função folhas que recebe uma lista para armazenar os nós folha
        if self.esquerda is None and self.direita is None:  # Verifica se o nodo atual é uma folha (não tem filhos)
            lst.append(self.dado)  # Adiciona o dado do nodo atual à lista
        if self.esquerda:  # Se existir um filho à esquerda
            self.esquerda.folhas(lst)  # Chama recursivamente a função folhas na subárvore esquerda
        if self.direita:  # Se existir um filho à direita
            self.direita.folhas(lst)  # Chama recursivamente a função folhas na subárvore direita
        return lst  # Retorna a lista contendo os dados dos nós folha

# Teste do programa
Teste = BST()  # Cria uma nova árvore binária de busca
Teste.inserir(7)  # Insere o dado 7 na árvore
Teste.inserir(4)  # Insere o dado 4 na árvore
Teste.inserir(9)  # Insere o dado 9 na árvore
Teste.inserir(0)  # Insere o dado 0 na árvore
Teste.inserir(5)  # Insere o dado 5 na árvore
Teste.inserir(8)  # Insere o dado 8 na árvore
Teste.inserir(13)  # Insere o dado 13 na árvore

print('Folhas: ', Teste.folhas([]))  # Imprime os dados dos nós folha da árvore
