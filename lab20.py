#!/usr/bin/env python3

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku
import copy

# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def quadrado(matriz, linha, coluna, numero):#funcao para verificar o quadrado do sudoku
    gomu = []
    pistol = []
    if (linha==0) or (linha==3) or (linha==6):
        gomu.append(linha)
        gomu.append(linha+1)
        gomu.append(linha+2)
    if (linha==1) or (linha==4) or (linha==7):
        gomu.append(linha)
        gomu.append(linha+1)
        gomu.append(linha-1)
    if (linha==2) or (linha==5) or (linha==8):
        gomu.append(linha)
        gomu.append(linha-2)
        gomu.append(linha-1)
    if (coluna==0) or (coluna==3) or (coluna==6):
        pistol.append(coluna)
        pistol.append(coluna+1)
        pistol.append(coluna+2)
    if (coluna==1) or (coluna==4) or (coluna==7):
        pistol.append(coluna)
        pistol.append(coluna+1)
        pistol.append(coluna-1)
    if (coluna==2) or (coluna==5) or (coluna==8):
        pistol.append(coluna)
        pistol.append(coluna-2)
        pistol.append(coluna-1)
    for line in gomu:
        for column in pistol:
            if numero==matriz[line][column]:
                return False
    return True
def verifica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                return False
    return True
def resolve(resposta):
    #copiar matriz
    outro = copy.deepcopy(resposta)
    if verifica(resposta):
        outro = copy.deepcopy(resposta)
        return True
    for linha in range(len(resposta)):
        for coluna in range(len(resposta[0])):#varia linha e coluna
            if resposta[linha][coluna] == 0:#verifica se o valor eh zero
                for numero in range(1,10):#se for vai verificar quais sao os possiveis valores para substituir
                    if numero not in resposta[linha]:#verifica se tem numero igual na linha
                        luffy = True
                        for linha2 in range(len(resposta)):#verifica se tem numero igual na coluna
                            if numero == resposta[linha2][coluna]:
                                luffy = False
                                break
                        if luffy and quadrado(resposta, linha, coluna, numero):
                            resposta[linha][coluna] = numero
                            if not resolve(resposta):
                                #print_sudoku(resposta)
                                resposta[linha][coluna] = 0
                            else:
                                return True
                                if verifica(resposta):
                                    outro = copy.deepcopy(resposta)
                                    return True
            if resposta[linha][coluna] == 0:
                resposta = copy.deepcopy(outro)
                return False
    # Implementar a funcao e trocar o valor de retorno
