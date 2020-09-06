#Patricia Amado F. de Mello
# 223085
'''Esse eh um programa que recebe dois parametros para leitura e salva parte deles para a execucao
de modificacoes nos pixels da imagem inicial, como um filtro de imagem.'''

import sys

imagemInicial = sys.argv[1] # Sempre comeca do [1]
matriz = sys.argv[2]

arquivoInicial = open(imagemInicial, "r") # Abrir para leitura a foto
arquivoMatriz = open(matriz, "r") # Abrir para leitura o texto

# Leitura do primeiro arquivo
p = arquivoInicial.readline().split() # Primeira linha que sera salvo o p
m,n = arquivoInicial.readline().split() # Pegando o tamanho da matriz
m,n = [int(m), int(n)]
pix = arquivoInicial.readline() # Linha referente ao maximo de pixel
mat = []
for a in range(n): # Numero de linhas
    b = arquivoInicial.readline().split()
    b = [int(x) for x in b]
    mat.append(b)

# Leitura do segundo arquivo
D = arquivoMatriz.readline() # Linha referente ao divisor
nucleo = []
for c in range(3): # Dimensao padrao do exercicio
    e = arquivoMatriz.readline().split()
    e = [int(x) for x in e]
    nucleo.append(e)
# Salvando as posicoes do nucleo com a nomenclatura da matriz nucleo do exercicio
a = nucleo[0][0] ; b = nucleo[0][1] ; c = nucleo[0][2]
d = nucleo[1][0] ; e = nucleo[1][1] ; f = nucleo[1][2]
g = nucleo[2][0] ; h = nucleo[2][1] ; i = nucleo[2][2]

# Fazendo as transformacoes
novaMat = []
for x in range(0,n):
    novaLinha = [0]*m
    for y in range(0,m):
        if x == 0 or x == n-1: # Caso sejam os elementos dos cantos da matriz
            novaLinha = mat[x]
        elif (x != 0 and y == 0) or (x != 0 and y == m-1):
            novoPixel = mat[x][y]
            novaLinha[y] = novoPixel
        else: # Caso o elemento nao esteja nas extremidades
            #novoPixel = ((a*mat[x-1][y-1])+(b*mat[x][y-1])+(c*mat[x+1][y-1])+(d*mat[x-1][y])+(e*mat[x][y])+(f*mat[x+1][y])+(g*mat[x-1][y+1])+(h*mat[x][y+1])+(i*mat[x+1][y+1]))/int(D)
            novoPixel = ((a*mat[x-1][y-1])+(b*mat[x-1][y])+(c*mat[x-1][y+1])+(d*mat[x][y-1])+(e*mat[x][y])+(f*mat[x][y+1])+(g*mat[x+1][y-1])+(h*mat[x+1][y])+(i*mat[x+1][y+1]))/int(D)
            novoPixel = int(novoPixel)
            if novoPixel < 0:
                novoPixel = 0 # Valor minimo
            elif novoPixel > 255:
                novoPixel = 255 # Valor maximo
            novaLinha[y] = novoPixel
    novaMat.append(novaLinha)

print(p[0])
print(m,n)
print(pix, end="")
for i in range(0,n):
    for j in range(0,m):
        print(novaMat[i][j], end=" ")
    print(" ")
