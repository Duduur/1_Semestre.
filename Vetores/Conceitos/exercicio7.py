vetor = [1,12,24,50,60,200]


for i in range(5):
    numeros = int(input("Digite um numero: "))

    posicao = 0

    while posicao < len(vetor) and vetor[posicao] < numeros:
        posicao +=1
    vetor.insert(posicao, numeros)
print("vetor final", vetor)