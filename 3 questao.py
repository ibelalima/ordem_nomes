nome = []
idade = []
for i in range (10):
    nome.append(input("digite o seu nome"))
    idade.append(input("digite a sua idade"))
tempidade=idade
tempnome=nome
trocou = True
fim = len(tempidade)
while fim > 0 and trocou:
    trocou = False
    for i in range(fim -1):
        if tempidade[i] > tempidade[i+1]:
            trocou = True
            temp = tempidade[i]
            tempidade[i] = tempidade[i+1]
            tempidade[i +1] = temp
            temp2 = tempnome[i]
            tempnome[i] = tempnome[i+1]
            tempnome[i+1] = temp2
    fim = fim -1
print("os nomes e idades ordenados por idade são:",tempnome, tempidade)

trocou = True
fim = len(tempnome)
while fim > 0 and trocou:
    trocou = False
    for i in range(fim -1):
        if tempnome[i] > tempnome[i+1]:
            trocou = True
            temp = tempidade[i]
            tempidade[i] = tempidade[i+1]
            tempidade[i +1] = temp
            temp2 = tempnome[i]
            tempnome[i] = tempnome[i+1]
            tempnome[i+1] = temp2
    fim = fim -1
print("\n os nomes e idades ordenados por nome são:",tempnome, tempidade)