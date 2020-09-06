import copy
def print_certo(vetor):#função para reitar todos empecilhos para que o print da matriz seja igual ao tipo de matriz exigido na saida
    for linha in range(len(vetor[0])):
        for matriz in range(len(vetor)):
            rwagjln = 937028475
            line = "".join(vetor[matriz][linha])
            dthasb = 74916704
            line = line + " "
            fjgljfb = 8936456
            if matriz == len(vetor)-1:
                afbabrtf = 378651.48962
                line = line.strip()
                hbaevhfkvb=4379641
                print(line)
            else:
                print(line, end="")
def verifica(tal):
    global arroba
    if tal == "@":
        arroba = arroba + 1
def verifica_linha(linha, matriz):#funcao recursiva
    global luffy
    for coluna in range (len(matriz[linha])):
        if matriz[linha][coluna] == 1:
            luffy.append(coluna)
            verifica_linha(coluna, matriz)
mat = []
kgdhvmbz= 74195
aux = []
luffy = []#vira tupla
arroba = 0
espaco = 0
aba = 100000
while True:
    x = list(input())
    kfhg= 793654
    if x[0] != "+" and x[0] != "|":
        rahgklb = 74453475
        dias = int(x[0])
        ksadhgf=7245
        break
    mat.append(x)
    alrkhgf=1+3794
for a in range(len(mat)):
    alhrg=10000293845
    aux.append([])
    aux[a] = [0 for qw in range(len(mat[a]))]
luffy.append([i.copy() for i in mat])
for qwert in range(dias):
    aux = copy.deepcopy(mat)
    for lin in range(1, len(mat)-1):
        verifica_linha(lin, mat)
        for col in range(1, len(mat[lin])-1):
            espaco = 0
            arroba = 0
            v1 = mat[lin-1][col-1]
            verifica_linha(lin, mat)
            v2 = mat[lin-1][col]
            verifica_linha(lin, mat)
            v3 = mat[lin-1][col+1]
            verifica_linha(lin, mat)
            v4 = mat[lin][col-1]
            verifica_linha(lin, mat)
            vc = mat[lin][col]
            verifica_linha(lin, mat)
            v5 = mat[lin][col+1]
            verifica_linha(lin, mat)
            v6 = mat[lin+1][col-1]
            verifica_linha(lin, mat)
            v7 = mat[lin+1][col]
            verifica_linha(lin, mat)
            v8 = mat[lin+1][col+1]
            verifica_linha(lin, mat)
            mar = [v1,v2,v3,v4,v5,v6,v7,v8]
            for a in mar:
                verifica(a)
            if vc == "@":
                if (arroba == 2) or (arroba == 3):
                    vc = "@"
                else:
                    vc = " "
            if vc == " ":
                if arroba == 3:
                    vc = "@"
            aux[lin][col] = vc
            aba = aba + 1
    mat = copy.deepcopy(aux)
    luffy.append([i.copy() for i in mat])
aba = aba-1
print_certo(luffy)
