# Forma que eu fiz
# vetor = [3, 7, 10, 15]
# numero = int(input("Digite um numero: "))

# for i in vetor:
#     if numero == i:
#         print("DEU CERTO", numero )
#         break

#Forma da professora

v = [3, 7, 10, 15]

valor = int(input("Digite um numero: "))

encontrou = False
for i in range(len(v)):
    if v[i] == valor:
        print("Valor encontrado na posição", i)
        encontrou = True
        break
if encontrou == False:
    print("Valor nao encontrado")
