#nome:Enzo Hideki Iwata    Ra:215394
def print_certo(matriz):#função para reitar todos empecilhos para que o print da matriz seja igual ao tipo de matriz exigido na saida
    for a in range(len(matriz)):
        line = matriz[a]
        line_print = str(line)
        line_print = line_print.strip("[]")
        line_print = "".join(line_print)
        line_print = line_print.replace(", ", "")
        print(line_print)
def insere0(matriz):#função para inserir os 0s na matriz(rodear a matriz com 0s
    linha1 = [0 for i in range (colunas)]
    matriz.insert(0,linha1)
    matriz.append(linha1)
    for a in range(linhas+1):
        matriz[a].insert(0,0)
        matriz[a].insert(colunas+1,0)
def retira0 (matriz):#função para retirar os 0 da matriz
    del matriz[0]
    del matriz[len(matriz)-1]
    for a in range(linhas):
        del matriz[a][0]
        del matriz[a][len(matriz[a])-1]
def copia(matriz1, matriz2):#função para copiar uma matriz na outra sem haver ligações enre elas
    for l in range(linhas+2):
        for c in range(colunas+2):
            matriz1[l][c] = matriz2[l][c]
def problema(matriz):#função para fazer as iterações do dia atual
    copia(matriz_aux, matriz)
    for lin in range(1, linhas+1):
        for col in range(1, colunas+1):
            v1 = matriz[lin-1][col-1]
            v2 = matriz[lin-1][col]
            v3 = matriz[lin-1][col+1]
            v4 = matriz[lin][col-1]
            vc = matriz[lin][col]
            v5 = matriz[lin][col+1]
            v6 = matriz[lin+1][col-1]
            v7 = matriz[lin+1][col]
            v8 = matriz[lin+1][col+1]
            mar = [v1,v2,v3,v4,v5,v6,v7,v8]
            valor = False
            humano = 0
            count = 0
            vcdia = vc
            for i in range(len(mar)):
                viz = mar[i]
                if vc == 1 and viz == 2:#centro igual a um humano
                    vcdia = 2
                if vc == 2:#centro igual a um zumbi
                    valor = True
                    if viz == 1:
                        humano = humano + 1
                if vc == 0:#centro vazio
                    if viz == 1:
                        count = count + 1
            if count == 2:
                vcdia = 1
            if valor:
                if humano != 1:
                    vcdia = 0
            matriz_aux[lin][col] = vcdia
    copia(matriz, matriz_aux)
var = input()#numero de linhas e colunas
ints = [int(i) for i in var.split()]#separa a variavel da linha e da coluna
linhas = ints[0]#linhas = primeiro termo
colunas = ints[1]#coluna = segundo termo
dias = int(input())#numero de dias
matriz = []
for li in range(linhas):#transforma a matriz entrada para uma matriz de listas
    li = input()
    line = [int(i) for i in li.split()]
    matriz.append(line)
print("iteracao 0")#printa a interação 0
print_certo(matriz)
insere0(matriz)
dia = 0
matriz_aux=[[] for a in range(linhas+2)]#construção da matriz auxiliar
for a in range(linhas+2):
    for b in range(colunas+2):
        matriz_aux[a].append(0)
for i in range(dias):#iterações para cada dia
    dia = dia + 1#acumulador de dias
    problema(matriz)
    print("iteracao %d"%dia)
    retira0(matriz)
    print_certo(matriz)
    insere0(matriz)
          
                        
                
