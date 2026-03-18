#adiciona 5 valores em um vetor  e soma eles no final
vetor = []

soma = 0

for i in range(5):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

for i in range(len(vetor)):
    soma += vetor[i]
print("Soma dos elementos: ", soma)