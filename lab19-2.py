#nome: Enzo Hideki Iwata
#RA:215394
def entrada(mat):#funcao para ler as entradas de matriz
    for lin in range(linha):
        mat.append(list(input()))
    return (mat)
def deleta(matriz, linha, coluna):
    if matriz[linha][coluna] == "@":#se for @entra para verificar as situacoes
        matriz[linha][coluna] = "-"#transforma em traco
        matriz = deleta(matriz, linha-1, coluna)#verifica para cada posiivilidade, cima, baixo, direita, esquerda
        matriz = deleta(matriz, linha+1, coluna)
        matriz = deleta(matriz, linha, coluna+1)
        matriz = deleta(matriz, linha, coluna-1)
    return (matriz)#retorna a nova matriz
def print_certo(matriz):#função para reitar todos empecilhos para que o print da matriz seja igual ao tipo de matriz exigido na saida
    for a in matriz:
        line = "".join(a)
        print(line)
def insere0(matriz):#função para inserir os +s na matriz(rodear a matriz com +s)
    linhas = len(matriz)
    colunas = len(matriz[0])
    linha1 = ["+" for i in range (colunas)]
    matriz.insert(0,linha1)
    matriz.append(linha1)
    for a in range(linhas+1):
        matriz[a].insert(0,"+")
        matriz[a].insert(colunas+1,"+")
def retira0 (matriz):#função para retirar os + da matriz
    del matriz[0]
    del matriz[len(matriz)-1]
    linhas = len(matriz)
    for a in range(linhas):
        del matriz[a][0]
        del matriz[a][len(matriz[a])-1]
linha, coluna = input().split("x")
linha, coluna = int(linha), int(coluna)
matriz1 = []
matriz2 = []
matriz1 = entrada(matriz1)
matriz2 = entrada(matriz2)
while True:#loop infinito
    try:#acho que podia ter feito uma funcao mas so percebi no final, entao nao vou fazer, contudo fica a dica
        x,y = input().split(",")
        x,y = int(x), int(y)#entrada de linhas e colunas
        if x == "":
            break
        else:
            luffy = True# com o for a vai verificar se a matriz ja nao morreu
            insere0(matriz2)#insere +
            matriz2 = deleta(matriz2, x, y)#funcao recursiva
            retira0(matriz2)#retira +
            for a in matriz2:
                if "@" in a:
                    luffy = False
            print("Ataque em (%d,%d) do jogador 1" %(x, y))
            print_certo(matriz2)
            if luffy:
                break
        x,y = input().split(",")
        x,y = int(x), int(y)#entrada de linhas e colunas
        if x == "":
            break
        else:
            luffy = True# com o for a vai verificar se a matriz ja nao morreu
            insere0(matriz1)#insere +
            matriz1 = deleta(matriz1, x, y)#funcao recursiva
            retira0(matriz1)#retira +
            for a in matriz1:
                if "@" in a:
                    luffy = False
            print("Ataque em (%d,%d) do jogador 2" %(x, y))
            print_certo(matriz1)
            if luffy:
                break
    except ValueError:#caso so haja um ataque a segunda entrada da erro, isso concerta o erro
        break
