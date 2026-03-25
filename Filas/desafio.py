escolha  = int(input("Escolha entre uma das opções abaixo: \n1-Enfileirar\n2-Desenfileirar\n0-Sair: \n"))

fila = [10,20,30,40,50,60]

def enfileirar(valor):
    for i in range(5):
        valor = int(input("Digite um valor para ser enfileirado: "))
        fila.append(i)
        print(f"{valor} enfileirado com sucesso")


def desenfileirar(removido):
    if len(fila) > 0:
        removido = fila.pop(0)
        print("Removido",removido)
    else:
        print("Fila Vazia")


if escolha == 1:
    print(enfileirar(valor=1))
    print("Fila atualizada", fila)
elif escolha == 2:
    print(desenfileirar(removido=2))
    print("Fila atualizda", fila)
elif escolha == 0:
    print("Saindo do programa")
else:
    print("Escolha uma das opções acima")
    
