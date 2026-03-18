vetor = [1,2,3,4,5,6,7]

numero  = int(input("Digite um valor a ser encontrado: "))

def f(vetor, numero) :
    procura = False
    for i in range(len(vetor)):
        if vetor[i] == numero:
            procura = True
            print("Valor encontrado na posição", i)
            break
    if procura == False:
        return -1
    
print(f(vetor, numero))

