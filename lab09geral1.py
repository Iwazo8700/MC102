def print_certo(vetor):#função para reitar todos empecilhos para que o print da matriz seja igual ao tipo de matriz exigido na saida
    for linha in range(len(vetor[0])):
        for matriz in range(len(vetor)):
            line = "".join(vetor[matriz][linha])
            line = line + " "
            if matriz == len(vetor)-1:
                line = line.strip()
                print(line)
            else:
                print(line, end="")
def remove(parametro):
    global mar
    if parametro in mar:
        mar.remove(parametro)
        return True
    else:
        return False
def copia(matriz1, matriz2):
    for a in range(len(matriz1)):
        for b in range(len(matriz1[a])):
            matriz2[a][b]=matriz1[a][b]

    return matriz2
matriz = []
matriz_aux = []
outro = []
while True:
    linhax = list(input())
    if linhax[0] != "+" and linhax[0] != "|":
        dias = int(linhax[0])
        break
    matriz.append(linhax)
for a in range(len(matriz)):
    matriz_aux.append([])
    matriz_aux[a] = [0 for qw in range(len(matriz[a]))]
outro.append([i.copy() for i in matriz])
for qwert in range(dias):
    matriz_aux = copia(matriz, matriz_aux)
    for lin in range(1, len(matriz)-1):
        for col in range(1, len(matriz[lin])-1):
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
            if vc == "@":
                if remove("@"):#true=1,false=0
                    if remove("@"):#true=2,false = 1
                        if remove("@"):#true=3, false=2
                            if remove("@"):
                                vc = " "
                    else:
                        vc = " "
                else:
                    vc = " "
            elif vc == " ":
                if remove("@"):#true=1
                    if remove("@"):#true=2
                        if remove("@"):#true=3
                            if remove("@"):
                                vc = " "
                            else:
                                vc = "@"
            matriz_aux[lin][col] = vc
    matriz = copia(matriz_aux, matriz)
    outro.append([i.copy() for i in matriz])
print_certo(outro)
