#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome:Enzo Hideki Iwata
# RA:215394

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda) 
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario 
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
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
    return la, al, posx

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro 
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):
    # Implementar a funcao e trocar o valor de retorno
    xf = l + x
    for i in range (9, -1, -1):
        for a in range(x, xf):
            if mat[i][a] == 1:
                return i + 1
    return 0
# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
    if a + y > 10:
        return 0
    else:
        return 1

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro 
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):
    # Implementar a funcao
    px = x + l
    if px > 10:
        x = 10 - l
        px = x + l
    if px < 0:
        x = 0
        px = l
    if x < 0:
        x = 0
        px = x + l
    py = a + y
    for i in range (y, py):
        for j in range(x, px):
            mat[i][j] = 1
# Funcoes: atualiza_matriz
# 
#    mat: matriz do tabuleiro 
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):
    # Implementar a funcao e trocar o valor de retorno
    pont = 0
    uns = [1 for i in range(10)]
    for a in range(9, -1, -1):
        if mat[a] == uns:
            zeros = [0 for i in range(10)]
            pont = pont + 1
            mat.remove(uns)
            mat.append(zeros)
    return pont
