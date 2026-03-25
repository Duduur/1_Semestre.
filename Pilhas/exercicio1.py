# PILHA

capacidade = 5 
pilha = []

if len(pilha) < capacidade:
    pilha.append(10)
    print("Empilhado", pilha)
else:
    print("Pilha Cheia")

#Empilhar outro

pilha.append(20)
print("Empilhado", pilha)


#DESEMPLIHAR
if len(pilha) > 0:
    removido = pilha.pop()
    print("Desempilhado")
else:
    print("Pilha Vazia")

print("Pilha atual", pilha)


