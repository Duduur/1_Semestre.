# Adicionando a um vetor nao ordenado e fazendo um for para adicionar 5 numeros
vetor = []

for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

for i in range(len(vetor)): #Len é para saber quaal o tamanho do meu vetor
    print("Elementos", i, ":", vetor[i])