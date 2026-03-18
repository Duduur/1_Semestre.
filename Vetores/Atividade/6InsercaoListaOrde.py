vetor = [3,6,9,12,15,18,21]

for i in range(5):
    numero = int(input("Digite um valor: "))

    posicao = 0 

    while posicao < len(vetor) and vetor[posicao] < numero:
        posicao +=1 
    vetor.insert(posicao, numero)
print(vetor)