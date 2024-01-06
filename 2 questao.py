nome = []
while True:
    nome.append(input("digite um nome"))
    parar = int(input("digite 1 caso queira parar"))
    if parar == 1:
        break
trocou = True
tempnome = nome
fim = len(tempnome)
while fim > 0 and trocou:
    trocou = False
    for i in range(fim -1):
        if tempnome[i] > tempnome[i+1]:
            trocou = True
            temp2 = tempnome[i]
            tempnome[i] = tempnome[i+1]
            tempnome[i+1] = temp2
    fim = fim -1
print(tempnome)