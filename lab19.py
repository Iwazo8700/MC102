#nome:Enzo Hideki Iwata
#RA:215394
def verifica_linha(linha, matriz):#funcao recursiva
    global luffy
    for coluna in range (len(matriz[linha])):
        if matriz[linha][coluna] == 1:
            luffy.append(coluna)
            verifica_linha(coluna, matriz)#na coluna em que tem funcionario transforma esse numero em llinha para se verificar na funcao
def ordena(vet):#selection sort
    for i in range(len(vet)):
        menor = i
        for j in range(i, len(vet)):
            if vet[j] < vet[menor]:
                menor = j
        vet[i],vet[menor] = vet[menor], vet[i]
    return vet
inte = input()
piece = [int(i) for i in inte.split()]
line = piece[1]
vetor = []
luffy = []
final = []
entrada = input()
while True:#entrada, se der eof quer dizer que acabaram as entradas
    vetor.append([int(i) for i in entrada.split()])
    try:
        entrada = input()
    except EOFError:
        break
verifica_linha(line, vetor)
luffy = ordena(luffy)
luffy = [line] + luffy#soma o primeiro com os funcionarios subordinados
final = str(luffy)#arruma o print
final = final.strip("[]")
final = "".join(final)
final = final.replace(", ", " ")
print(final)
