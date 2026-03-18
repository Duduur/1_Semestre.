vetor = [2, 5,8,12]

novo_valor = int(input("Digite um valor: "))

posicao = 0

while posicao < len(vetor) and vetor[posicao] < novo_valor:
    posicao +=1
vetor.insert(posicao, novo_valor)
print("vetor final", vetor)