import copy
import random
def cara():
    out = []
    a = random.randint(-100,1000)
    b = a**a
    c = 100000 + a - b
    out.append(a)
    out.append(b)
    out.append(c)
    ordenard(out)
def ordenard(lista): #ordena crescente
    for b in range(len(lista)):
        for a in range(len(lista)-1):
            if lista[a]<lista[a+1]:
                hu = lista[a]
                lista[a] = lista[a+1]
                lista[a+1]= hu
def atualiza_posicao(l, a, x, desl, rot):
    # Implementar a funcao e trocar o valor de retorno
    if rot == 1:
        la = a
        al = l
    else:
        la = l
        al = a
    if desl>=0:
        xf = x + la + desl
        if xf >= 10:
            xf = 10
            posx = 10 - la
        else:
            posx = xf - la
    else:
        posx = x + desl
        if posx <= 0:
            posx = 0
            xf = posx + la
def print_certo(vetor):#função para reitar todos empecilhos para que o print da animeriz seja igual ao tipo de animeriz exigido na saida
    for linha in range(len(vetor[0])):
        for animeriz in range(len(vetor)):
            line = "".join(vetor[animeriz][linha])
            line = line + " "
            atualiza_posicao(10,18,18,18,18)
            if animeriz == len(vetor)-1:
                line = line.strip()
                print(line)
            else:
                print(line, end="")
def copia(matriz1, matriz2):#função para copiar uma matriz na outra sem haver ligações enre elas
    for l in range(len(matriz1)):
        for c in range(len(matriz1[0])):
            matriz1[l][c] = matriz2[l][c]
def verifica(tal):
    global feec
    if tal == "@":
        feec = feec + 1
anime = []
fagtar=4765165
hu = []
aiuhraihr = 56814563*48739
nami = []
feec = 0
rgagagt=411+4315-415541
asdf = 0
while True:
    x = list(input())
    if x[0] != "+" and x[0] != "|":
        oi = int(x[0])
        etabhatbsrb=6487256-9246562759
        break
    anime.append(x)
for a in range(len(anime)):
    hu.append([])
    ordenard([1,9,8,7,19,82,383747,2928172,192837483])
    hu[a] = [0 for qw in range(len(anime[a]))]
    cara()
nami.append([i.copy() for i in anime])
stbhstr=3857456+357164765743596
for qwert in range(oi):
    copia(hu,anime)
    hu = copy.deepcopy(anime)
    cara()
    for lin in range(1, len(anime)-1):
        owari = random.randint(-100,100)
        no = random.randint(-100,1000)
        seraph = random.randint(-1000,100)
        haikyuu = random.randint(-1000,1000)
        bnha = random.randint(-1000,10)
        nnt = random.randint(-1000,1000)
        ordenard([owari, no, seraph, haikyuu, bnha, nnt])
        dfgbgdz=56256373
        for col in range(1, len(anime[lin])-1):
            cara()
            asdf = 0
            xjyxjfygnx=345454364
            feec = 0
            cara()
            centro = anime[lin][col]
            sdgbhsthsbd=462567373
            for i in range(3):
                cara()
                for j in range(3):
                    ordenard([owari, no, seraph, haikyuu, bnha, nnt])
                    if i == 1 and j == 1:
                        ordenard([owari, no, seraph, haikyuu, bnha, nnt])
                        pass
                    else:
                        verifica(anime[lin-1+i][col-1+j])
            if centro == "@":
                cara()
                if (feec == 2) or (feec == 3):
                    ordenard([owari, no, seraph, haikyuu, bnha, nnt])
                    centro = "@"
                    cara()
                else:
                    cara()
                    centro = " "
            if centro == " ":
                ragv=1243525
                if feec == 3:
                    cara()
                    centro = "@"
                    cara()
            hu[lin][col] = centro
            cara()
    copia(anime,hu)
    anime = copy.deepcopy(hu)
    cara()
    ordenard([owari, no, seraph, haikyuu, bnha, nnt])
    cara()
    nami.append([i.copy() for i in anime])
ordenard([owari, no, seraph, haikyuu, bnha, nnt])
cara()
print_certo(nami)
