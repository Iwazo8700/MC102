
def print_bingo(vet):
    print("+----------------+\n| B  I  N  G  O  |\n+================+")
    for i in range(5):
        print("| ", end="")
        for j in range(5):
            print(vet[i][j],"",end="")
        print("|")
    print("+----------------+")

def verifica_bingo(vet):
    linha = 0
    coluna = 0
    diagonal = 0
    for i in range(5):
        coluna = 0
        linha = 0
        for j in range(5):
            if(vet[i][j] == "XX"):
                linha = linha + 1
            else:
                linha = 0
            if(vet[j][i] == "XX"):
                coluna = coluna + 1
            else:
                coluna = 0
            if (coluna == 5 or linha == 5):
                return True
    if(vet[0][4] == "XX" and vet[1][3] == "XX" and vet[3][1] == "XX" and vet[4][0] == "XX"):
        return True
    if(vet[0][0] == "XX" and vet[1][1] == "XX" and vet[3][3] == "XX" and vet[4][4] == "XX"):
        return True
    return False

def muda_bingo(vet, num, entrada, char):
    for i in range(5):
        if(vet[i][num] == entrada):
            vet[i][num] = "XX"
            print_bingo(vet)
    return vet

def main():
    matriz = [ [0 for j in range(5)] for i in range (5)]
    for x in range(5):
       matriz[x] = [a for a in input().split()]
    print_bingo(matriz)
    num = int(input())
    for i in range(num):
        linha = input().split("-")
        print(linha[0]+"-"+linha[1])
        if(linha[0] == "B"):
            matriz = muda_bingo(matriz, 0, linha[1], "B")
        elif(linha[0] == "I"):
            matriz = muda_bingo(matriz, 1, linha[1], "I")
        elif(linha[0] == "N"):
            matriz = muda_bingo(matriz, 2, linha[1], "N")
        elif(linha[0] == "G"):
            matriz = muda_bingo(matriz, 3, linha[1], "G")
        elif(linha[0] == "O"):
            matriz = muda_bingo(matriz, 4, linha[1], "O")
        if(verifica_bingo(matriz)):
            print("BINGO!")
            break

main()
