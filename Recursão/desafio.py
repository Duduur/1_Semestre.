
def expoente (b, p): 
    if p == 0:
        return 1
    return b * expoente(b ,p-1)

print(expoente(5,3))

b =2
p=3

for base in range(b):
    resultado = 1
    for potencia in range(p):
         resultado *= b
print(resultado)

total = 1
for i in range(1, p+1):
    total *=b
print(total)