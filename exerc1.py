"""
Exercicio 01 da atividade pratica de Estrutura de dados.
LEANDRO PRAZERES COELHO
RU: 3867885
"""
def mergeSort(dados):  # Define a função mergeSort que recebe a lista 'dados' como argumento
    if len(dados) > 1:  # Verifica se o comprimento da lista 'dados' é maior que 1
        meio = len(dados) // 2  # Calcula o ponto médio da lista
        esquerda = dados[:meio]  # Divide a lista em duas metades, a metade esquerda
        direita = dados[meio:]  # e a metade direita

        mergeSort(esquerda)  # Chama a função recursivamente para a metade esquerda
        mergeSort(direita)  # Chama a função recursivamente para a metade direita

        i = j = k = 0  # Inicializa os índices para percorrer as listas 'esquerda', 'direita' e 'dados'

        while i < len(esquerda) and j < len(direita):  # Percorre ambas as listas enquanto houver elementos em ambas
            if esquerda[i] >= direita[j]:  # Compara os elementos de 'esquerda' e 'direita'
                dados[k] = esquerda[i]  # Coloca o elemento maior na posição k de 'dados'
                i += 1  # Avança para o próximo elemento em 'esquerda'
            else:
                dados[k] = direita[j]  # Coloca o elemento maior na posição k de 'dados'
                j += 1  # Avança para o próximo elemento em 'direita'
            k += 1  # Avança para a próxima posição em 'dados'

        while i < len(esquerda):  # Verifica se ainda restam elementos em 'esquerda'
            dados[k] = esquerda[i]  # Copia os elementos restantes de 'esquerda' para 'dados'
            i += 1  # Avança para o próximo elemento em 'esquerda'
            k += 1  # Avança para a próxima posição em 'dados'

        while j < len(direita):  # Verifica se ainda restam elementos em 'direita'
            dados[k] = direita[j]  # Copia os elementos restantes de 'direita' para 'dados'
            j += 1  # Avança para o próximo elemento em 'direita'
            k += 1  # Avança para a próxima posição em 'dados'

# Teste da função
dados = [54, 26, 93, 17, 77, 31, 44, 55]  # Define a lista de dados a ser ordenada
print("Lista que será ordenada: ", "\n", dados, "\n")# Imprime a lista inicial (não ordenada ainda)
mergeSort(dados)  # Chama a função mergeSort passando a lista 'dados'
print("Lista ordenada usando a função mergeSort:","\n", dados)  # Imprime a lista ordenada


