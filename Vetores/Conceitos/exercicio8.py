
# Remove : remove por elemento
# Pop:  remove por posição

vetor = [2,4,6,8,10,12]

valor = int(input("Digite um numero: "))

if valor in vetor:
    #vetor.remove(valor)
    vetor.pop(valor)
    print(f"Elemento {valor} excluido com sucesso")
    print("Vetor após remoção: ", vetor)
else:
    print("Valor não encontrado")