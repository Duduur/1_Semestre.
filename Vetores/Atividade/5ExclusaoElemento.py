vetor = [2,4,6,8,10,12]

valor = int(input("Digite o indece para exlusao: "))

def exclusao(vetor, valor):
    if valor < len(vetor):
        vetor.pop(valor)
        print(f"Elemento {valor} excluido com sucesso")
        print("Vetor após remoção: ", vetor)
    else:
        print("Valor não encontrado")

exclusao(vetor, valor)