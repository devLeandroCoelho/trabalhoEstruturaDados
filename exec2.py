import random  # Importa o módulo random para utilizar a função de embaralhamento

def embaralhaCartas(baralho):  # Define a função embaralhaCartas que recebe a lista 'baralho'
    baralhoEmbaralhado = baralho[:]  # Cria uma cópia da lista 'baralho' para não modificar a original
    n = len(baralhoEmbaralhado)  # Armazena o comprimento da lista
    for i in range(n - 1, 0, -1):  # Percorre a lista de trás para frente
        j = (i + 1) % n  # Calcula um índice 'j' baseado na posição 'i' e o comprimento da lista
        baralhoEmbaralhado[i], baralhoEmbaralhado[j] = baralhoEmbaralhado[j], baralhoEmbaralhado[i]  # Troca os elementos na posição 'i' e 'j'
    return baralhoEmbaralhado  # Retorna a lista embaralhada

def compraCartas(pilhaCartas):  # Define a função compraCartas que recebe a lista 'pilhaCartas'
    if pilhaCartas:  # Verifica se a lista 'pilhaCartas' não está vazia
        carta = pilhaCartas.pop()  # Remove a última carta da lista e a armazena em 'carta'
        print(carta, "\n")  # Imprime a carta retirada
    else:
        print("Não há mais cartas na pilha.")  # Informa que não há mais cartas se a lista estiver vazia

# Lista de cartas do baralho original e lacrado de fabrica
baralho = ["A-Copas", "A-Paus", "A-Espadas", "A-Ouros",
           "2-Copas", "2-Paus", "2-Espadas", "2-Ouros",
           "3-Copas", "3-Paus", "3-Espadas", "3-Ouros",
           "4-Copas", "4-Paus", "4-Espadas", "4-Ouros",
           "5-Copas", "5-Paus", "5-Espadas", "5-Ouros",
           "6-Copas", "6-Paus", "6-Espadas", "6-Ouros",
           "7-Copas", "7-Paus", "7-Espadas", "7-Ouros",
           "8-Copas", "8-Paus", "8-Espadas", "8-Ouros",
           "9-Copas", "9-Paus", "9-Espadas", "9-Ouros",
           "10-Copas", "10-Paus", "10-Espadas", "10-Ouros",
           "J-Copas", "J-Paus", "J-Espadas", "J-Ouros",
           "Q-Copas", "Q-Paus", "Q-Espadas", "Q-Ouros",
           "K-Copas", "K-Paus", "K-Espadas", "K-Ouros"]

# Teste das funções
pilhaCartas = embaralhaCartas(baralho)  # Chama a função embaralhaCartas passando a lista 'baralho' e armazena o resultado em 'pilhaCartas'

print("Pilha de Cartas não embaralhadas: ", "\n", baralho, "\n")# Imprime a Pilha de Cartas ainda não embaralhadas

print("Pilha de Cartas embaralhadas: ", "\n", pilhaCartas, "\n")# Imprime a Pilha de Cartas já embaralhadas

for compras in range(3):  # Usa um loop for para chamar a função compraCartas três vezes
    print(compras + 1, "ª Carta comprada: ") # print apanas para informar a quantidade de compra da carta
    compraCartas(pilhaCartas)  # Chama a função compraCartas passando a lista 'pilhaCartas'


