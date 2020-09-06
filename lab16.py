# coding=utf-8
#  Funcao: removePalavras
#
#nome: Enzo Hideki Iwata
#RA: 215394
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
#
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
    s = s.split(" ")#transformo tudo em lista
    cont = 0
    for a in range(len(s)):
        a = a - cont
        if s[a] in vs:# caso encontro algo para deletar eu deleto
            del s[a]
            cont = cont + 1
    s = " ".join(s)#transformo em string
    s = s.strip()
    return s

#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada pagina em paginas contem todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	entao deve-se atribuir 1 para resp[i] e 0 caso nao contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(palavrasPagina, termosBusca):
    lista = []
    v = False
    for frase in palavrasPagina:#laço encaixado para verificar a acorrencia de cada palavra
        frase = frase.split()
        for termo in termosBusca:
            if termo in frase:
                v = True
            else:
                v = False #se um dos termos ja não estiver dá break e append 0
                break
        if v:
            lista.append(1)
        else:
            lista.append(0)
    return lista


#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
    final = []
    cont = 0
    for i in range(len(resp)):#faz uma lista para verificar as ocorrencias de 0 e deleta a posição dessa ocorrencia na matriz
        if resp[i]==0:
            final.append(-1)
            i = i - cont
            del links[i]
            cont = cont + 1
        else:
            final.append(0)
    try:
        for a in range(len(links[0])):#laço encaixado para variar primeiro linha depois coluna
            if final[a] == 0:
                acu = 0
                for linha in range(len(links)):#acumula os uns que tem na coluna de matriz de links que direcionam para o lugar certo
                    acu = acu + links[linha][a]
                final[a] = acu
    except IndexError:
        return final
    return final
