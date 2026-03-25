fila = []
while True:
    print("1 - Adicionar na fila")
    print("2 - Desenfileirar a fila")
    print("3 - SAIR")
    o = int(input("Digite a opção desejada"))
    if o == 1:
        o1 = input("Digite o numero que deseja adicionar na fila: ")
        fila.append(o1)
        print("Fila Atual", fila)
    elif o == 2:
        remove = fila.pop(0)
        print("Removido:", remove)
    elif o == 3:
        print("Voce saiu")
        break
    else:
        print("Opção invalida")
        