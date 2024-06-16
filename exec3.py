class ElementoDaListaSimples:
    def __init__(self, dado, cor):  # Inicializa um novo nodo da lista com dado e cor
        self.dado = dado  # Armazena o dado do paciente
        self.cor = cor  # Armazena a cor do cartão (V ou A)
        self.proximo = None  # Inicializa o ponteiro para o próximo nodo como None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):  # Inicializa uma nova lista encadeada simples
        self.head = None  # Inicializa o cabeçalho da lista como None

    def inserirNoFinal(self, nodo):  # Insere um nodo no final da lista
        if self.head is None:  # Se a lista estiver vazia
            self.head = nodo  # O nodo se torna o cabeçalho da lista
            return
        nodo_atual = self.head  # Começa do cabeçalho da lista
        while nodo_atual.proximo is not None:  # Percorre a lista até encontrar o último nodo
            nodo_atual = nodo_atual.proximo  # Avança para o próximo nodo
        nodo_atual.proximo = nodo  # Insere o novo nodo no final da lista
        return

    def inserirPrioridade(self, nodo):  # Insere um nodo com prioridade na lista
        if self.head is None or self.head.cor == "V":  # Se a lista estiver vazia ou o primeiro nodo for verde
            nodo.proximo = self.head  # O novo nodo aponta para o cabeçalho atual
            self.head = nodo  # O novo nodo se torna o cabeçalho da lista
            return
        nodo_atual = self.head  # Começa do cabeçalho da lista
        while nodo_atual.proximo is not None and nodo_atual.proximo.cor == "A":  # Percorre a lista até encontrar um nodo verde ou o final da lista
            nodo_atual = nodo_atual.proximo  # Avança para o próximo nodo
        nodo.proximo = nodo_atual.proximo  # O novo nodo aponta para o próximo nodo do nodo_atual
        nodo_atual.proximo = nodo  # O nodo_atual aponta para o novo nodo
        return

    def inserir(self, dado, cor):  # Insere um novo paciente na lista com base na cor do cartão
        nodo = ElementoDaListaSimples(dado, cor)  # Cria um novo nodo com o dado e a cor fornecidos
        if self.head is None:  # Se a lista estiver vazia
            self.head = nodo  # O novo nodo se torna o cabeçalho da lista
            return
        else:
            if nodo.cor == "V":  # Se o cartão for verde
                self.inserirNoFinal(nodo)  # Insere o nodo no final da lista
            else:
                self.inserirPrioridade(nodo)  # Insere o nodo com prioridade
            return

# Teste do programa
filaPacientes = ListaEncadeadaSimples()  # Cria a lista que irá receber os dados dos pacientes
filaPacientes.inserir(1, "V")  # Insere um paciente com cartão "V" e senha 1
filaPacientes.inserir(2, "V")  # Insere um paciente com cartão "V" e senha 2
filaPacientes.inserir(101, "A")  # Insere um paciente com cartão "A" e senha 101
filaPacientes.inserir(3, "V")  # Insere um paciente com cartão "V" e senha 3
filaPacientes.inserir(102, "A")  # Insere um paciente com cartão "A" e senha 102
filaPacientes.inserir(103, "A")  # Insere um paciente com cartão "A" e senha 103
filaPacientes.inserir(4, "V")  # Insere um paciente com cartão "V" e senha 4
filaPacientes.inserir(104, "A")  # Insere um paciente com cartão "A" e senha 104
filaPacientes.inserir(105, "A")  # Insere um paciente com cartão "A" e senha 105

# Imprime a lista de pacientes na ordem de atendimento
nodo_atual = filaPacientes.head
while nodo_atual is not None:  # Percorre toda a lista de pacientes
    print(f"Cartão: {nodo_atual.cor}, Senha: {nodo_atual.dado}")  # Imprime a cor do cartão e a senha do paciente
    nodo_atual = nodo_atual.proximo  # Avança para o próximo nodo na lista
