import sys, os
import copy
sys.path.insert(0,os.getcwd())
#nome: Enzo Hideki Iwata
#RA:215394

def ler_imagem(nome_arquivo):#funcao para pegar o arquivo e ler(imagem)
    global imagem
    global linha
    global coluna
    global arq1
    piece = 0
    while True:
        line = arq1.readline()
        if line == "":
            break
        if piece == 1:
            lista = [int(i) for i in line.split()]
            linha = lista[1]
            coluna = lista[0]
        if piece > 2:
            imagem.append([int(i) for i in line.split()])
        piece = piece + 1
    arq1.close()
def ler_matriz(nome_matriz):#funcao para ler a matriz
    global divisor
    global matriz
    global arq2
    luffy = 0
    while True:
        line = arq2.readline()
        if line == "":
            break
        if luffy == 0:
            divisor = int(line)
        if luffy > 0:
            matriz.append([int(i) for i in line.split()])
        luffy = luffy + 1
    arq2.close()
def operacao(x, y):#funcao para fazer a operacao matematica
    global imagem
    global matriz
    soma = 0
    for a in range(3):
        for b in range(3):
            soma = soma + (matriz[a][b]*imagem[x+a][y+b])
    return (soma)
def print_certo(line):
    line = str(line)
    line = line.strip("[]")
    line = "".join(line)
    line = line.replace(", ", " ")
    line = line + "  "
    print(line)
def protagonista():#funcao que executa o programa
    for lin in range(linha):
        for col in range(coluna):
            if (lin == 0) or (col == 0) or (lin == linha - 1) or (col == coluna - 1):
                auxiliar[lin][col] = ((imagem[lin][col]))
            else:
                auxiliar[lin][col] = copy.copy((operacao(lin-1,col-1))//divisor)
                if auxiliar[lin][col] > 255:
                    auxiliar[lin][col] = 255
                if auxiliar[lin][col] < 0:
                    auxiliar[lin][col] = 0
        print_certo(auxiliar[lin])
imagem = []
matriz = []
auxiliar = []
divisor = 0
linha = 0
coluna = 0
arq1 = open(sys.argv[1],"r")
ler_imagem(arq1)
arq2 = open(sys.argv[2],"r")
ler_matriz(arq2)
zoro = [0]*coluna
auxiliar = []
print("P2")
print(coluna, linha)
print("255")
for lin in range(linha):
    auxiliar.append(zoro)
protagonista()
