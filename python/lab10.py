#nome: Enzo Hideki Iwata    RA:215394
texto = input()#texto primeiro
print(texto)
sep = texto.split()# separação do texto1 para uma lista(lista com letras maiusculas e minusculas)
teste = texto.lower()#texto1 em letra minuscula para facilitar as comparações
comando = input()#comando
sep1 = teste.split()#lista com letra minuscula
while comando != "Q":
    palavra = input()#palavra paar executar o comando
    teste2 = palavra.lower()#texto substituto para comprações
    teste = texto.lower()#texto1 em letra minuscula para facilitar as comparações
    inv = ""#função inverter
    cont = 0
    if comando == "D" :#comando deletar
        tam = len(sep)#tamanho atual da lista do texto 1
        De = teste2 + "!"#palavras mais as pontuações para indentificar a palavra que está na lista1
        Di = teste2 + "?"
        Dp = teste2 + "."
        Dv = teste2 + ","
        D2p = teste2 + ":"
        D = teste2
        for i in range(tam):#comparação de cada palavra da lista1 com a palavra comando mais cada sinal
            i = i - cont
            if sep1[i] == De or sep1[i] == Di or sep1[i] == Dp or sep1[i] == Dv or sep1[i] == D2p or sep1[i] == D:            
                del sep[i]
                del sep1[i]#deleto a palavra na posição em que ela foi encontrada como deletável
                cont = cont + 1
    if comando == "I":#comando inverter
        tam = len(sep)
        Ie = teste2 + "!"#adicionar os sinais para fazer a comparação com o termo da lista
        Ii = teste2 + "?"
        Ip = teste2 + "."
        Iv = teste2 + ","
        I2p = teste2 + ":"
        I = teste2
        for i in range(tam):#para cada if ele vai comparar o termo da lista(com ou sem sinal) para ver se é gual
            if sep1[i] == I:
                xis = len(palavra)
                for k in range(xis):#inversão da palavra
                    pal = sep[i]
                    letra = pal[xis - 1]
                    inv = inv + letra
                    xis = xis - 1
                sep[i] = inv#substituo a palavra que tinha antes pela sua invertida
                sep1[i] = inv
                inv = ""
            elif sep1[i] == Ii:
                xis = len(palavra)
                for k in range(xis):
                    pal = sep[i]
                    letra = pal[xis - 1]
                    inv = inv + letra
                    xis = xis - 1
                sep[i] = inv + "?"#adiciono o sinal que tinha no texto
                sep1[i] = inv + "?"
                inv = ""
            elif sep1[i] == Ip:
                xis = len(palavra)
                for k in range(xis):
                    pal = sep[i]
                    letra = pal[xis - 1]
                    inv = inv + letra
                    xis = xis - 1
                sep[i] = inv + "."
                sep1[i] = inv + "."
                inv = ""
            elif sep1[i] == Iv:
                xis = len(palavra)
                for k in range(xis):
                    pal = sep[i]
                    letra = pal[xis - 1]
                    inv = inv + letra
                    xis = xis - 1
                sep[i] = inv + ","
                sep1[i] = inv + ","
                inv = ""
            elif sep1[i] == I2p:
                xis = len(palavra)
                for k in range(xis):
                    pal = sep[i]
                    letra = pal[xis - 1]
                    inv = inv + letra
                    xis = xis - 1
                sep[i] = inv + ":"
                sep1[i] = inv + ":"
                inv = ""
    if comando == "R":#comando de substituição da palavra
        Re = teste2 + "!"
        Ri = teste2 + "?"
        Rp = teste2 + "."
        Rv = teste2 + ","
        R2p = teste2 + ":"
        R = teste2
        palavra2 = input()
        tam = len(sep)
        for i in range(tam):
            if sep1[i] == R:
                sep1[i] = palavra2#substituo a palavra atribuindo na posição em que está a palavra que se deseja tirar a palavra que se deseja colocar 
                sep[i] = palavra2
            elif sep1[i] == Re:
                sep1[i] = palavra2 + "!"
                sep[i] = palavra2 + "!"
            elif sep1[i] == Ri:
                sep1[i] = palavra2 + "?"
                sep[i] = palavra2 + "?"
            elif sep1[i] == Rp:
                sep1[i] = palavra2 + "."
                sep[i] = palavra2 + "."
            elif sep1[i] == Rv:
                sep1[i] = palavra2 + ","
                sep[i] = palavra2 + ","
            elif sep1[i] == R2p:
                sep1[i] = palavra2 + ":"
                sep[i] = palavra2 + ":"
    sep = " ".join(sep)#rearranjo para que se possa imprimir e deixra como lista novamente
    print(sep)
    sep = sep.split()
    comando = input()#novo comando
    sep1 = " ".join(sep1) 
    sep1 = sep1.lower()
    sep1 = sep1.split()
