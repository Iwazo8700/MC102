#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno
    conj = set(conj)
    if num in conj:
        return True
    else:
        return False


# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj1 = set(conj1)
    conj2 = set(conj2)
    final = conj1.intersection(conj2)
    if conj1 == final:
        return True
    else:
        return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao
    if not num in conj:
        conj = conj.append(num)

def subtracao(conj, num):
    # Implementar a funcao
    if num in conj:
        conj = conj.remove(num)

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj1 = set(conj1)
    conj2 = set(conj2)
    c = conj1.union(conj2)
    c = list(c)
    return [c]

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj1 = set(conj1)
    conj2 = set(conj2)
    c = conj1.intersection(conj2)
    c = list(c)
    return [c]

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj1 = set(conj1)
    conj2 = set(conj2)
    c = conj1.difference(conj2)
    c = list(c)
    return [c]

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj1 = set(conj1)
    conj2 = set(conj2)
    c = conj1.union(conj2)
    d = conj1.intersection(conj2)
    e = c.difference(d)
    e = list(e)
    return [e]
