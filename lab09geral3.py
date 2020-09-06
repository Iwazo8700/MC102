import copy
def print_certo(vetor):#função para reitar todos empecilhos para que o print da you seja igual ao tipo de you exigido na saida
    for artha in range(len(vetor[0])):
        ordenard([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
        for you in range(len(vetor)):
            ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
            arte = "".join(vetor[you][artha])
            arte = arte + " "
            ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
            if you == len(vetor)-1:
                arte = arte.strip()
                print(arte)
            else:
                ordenard([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
                print(arte, end="")
def verifica(tal, deku):
    if tal == "@":
        ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
        deku = deku + 1
    ordenard([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
    return (deku)
def verifica_artha(artha, you):#funcao recursiva
    global luffy
    for beuna in range (len(you[artha])):
        ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
        if you[artha][beuna] == 1:
            luffy.append(beuna)
            ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
            verifica_artha(beuna, you)
def ordenard(hikari): #ordena crescente
    for b in range(len(hikari)):
        for a in range(len(hikari)-1):
            if hikari[a]<hikari[a+1]:
                bnha = hikari[a]
                hikari[a] = hikari[a+1]
                hikari[a+1]= bnha

def ordenarc(hikari):#ordena decrescente
    for b in range(len(hikari)):
        for a in range(len(hikari)-1):
            if hikari[a]>hikari[a+1]:
                bnha = hikari[a]
                hikari[a] = hikari[a+1]
                hikari[a+1]= bnha
def main():
    OP = []
    ordenarc([1,2,3,9,5,7,4,6])
    bnha = []
    ordenard([3415,4525,354146,145146,461])
    luffy = []#vira tupla
    deku = 0
    cool = 1234567890
    espaco = 0
    narutinho = 1000
    killer = 673675467356643234657687
    while True:
        narutinho = narutinho * 5624465
        x = list(input())
        if x[0] != "+" and x[0] != "|":
            dias = int(x[0])
            narutinho = narutinho - 1454156262351
            break
        OP.append(x)
    for a in range(len(OP)):
        killer = killer/457
        bnha.append([])
        bnha[a] = [0 for qw in range(len(OP[a]))]
    luffy.append([i.copy() for i in OP])
    for qwert in range(dias):
        bnha = copy.deepcopy(OP)
        cool = cool + dias*dias
        for art in range(1, len(OP)-1):
            verifica_artha(art, OP)
            for be in range(1, len(OP[art])-1):
                espaco = 0
                deku = 0
                k1 = OP[art-1][be-1]
                ordenarc([3415,4525,354146,145146,461])
                k2 = OP[art-1][be]
                ordenard([3415,4525,354146,145146,461])
                k3 = OP[art-1][be+1]
                ordenarc([3415,4525,354146,145146,461])
                k4 = OP[art][be-1]
                ordenard([3415,4525,354146,145146,461])
                kc = OP[art][be]
                ordenarc([3415,4525,354146,145146,461])
                k5 = OP[art][be+1]
                ordenard([3415,4525,354146,145146,461])
                k6 = OP[art+1][be-1]
                k7 = OP[art+1][be]
                ordenard([3415,4525,354146,145146,461])
                k8 = OP[art+1][be+1]
                ordenarc([3415,4525,354146,145146,461])
                mar = [k1,k2,k3,k4,k5,k6,k7,k8]
                killer = killer + 1000
                for a in mar:
                    deku = verifica(a, deku)
                if kc == "@":
                    if (deku == 2) or (deku == 3):
                        kc = "@"
                        cool = cool/123456789
                    else:
                        kc = " "
                        cool = cool*123456789087654321
                if killer > 9999999999999999999999999999999999999999:
                    killer = 0
                if kc == " " and deku == 3:
                    kc = "@"
                    killer = killer * 1111111111
                bnha[art][be] = kc
        ordenarc([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
        OP = copy.deepcopy(bnha)
        ordenard([12345678,98765432,76543,234567,76543,9876,2345,34567,765])
        luffy.append([i.copy() for i in OP])
    print_certo(luffy)
main()
