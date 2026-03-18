def busca_binaria(vetor, valor):

    low = 0 #começa com o valor  da lista na posição 0 
    high = len(vetor) -1 # O high ele vai pegar o tamanho da lista e subtarir 1 porque o python é assim

    while low <= high:
        mid = (low + high)