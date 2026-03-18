
vetor = [2,3,4,5,2,5,7,2,1,8,9]
valor = int(input("Digite um valor: "))

contador = 0

for i in range(len(vetor)):
    if vetor[i] ==valor:
        contador +=1
print("O valor aparece" , contador, "vezes")