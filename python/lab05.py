#nome: Enzo Hideki Iwata    RA:215394
#O programa simulará uma luta no Street Fighter entre Ryu e Ken, as entradas serão relativas ao Ryu, em que valores positivos significam danos efetuados pelo personagem e valores negativos os danos levados pelo personagem, apos a mudança de golpe(sofrido ou exercido) haverá um print da atual vida do lutador assim como quando algum personagem morrer. serão dois rounds de luta, aquele que vencer duas lutas ganhará a disputa, se houver somente uma luta vencida a batalha será considerada como empate.
#primeiro round
r = 50
k = 50
p = int(input())
acu = 0
acu1 = 0
k1 = 1
r1 = 1
while k > 0 and r > 0:
    ki = k
    ri = r
    if k1 <= 0 or r1 <= 0:
        break
    else:
        while p > 0:#situação dos numeros positivos
            acu = acu + p
            k1 = k - p
            if k1 <= 0:
                print ("Ken:" ,ki, "-" ,acu, "=" ,k1)#ken derrotado
                k = k1
                break
            else:
                p = int(input())
                if p < 0 or k1 <= 0:
                    print ("Ken:" ,ki, "-" ,acu, "=" ,k1)
                    k = k1
                    acu = 0
                    break
                else:
                    k = k1
        while p < 0:#situação dos numeros negativos
            acu1 = acu1 - p
            r1 = r + p
            if r1 <= 0:
                print("Ryu:" , ri, "-" ,acu1, "=" ,r1)#ryu derrotado
                r = r1
                break
            else:
                p = int(input())
                if p > 0 or r1 <= 0:
                    print("Ryu:" , ri, "-" ,acu1, "=" ,r1)
                    r = r1
                    acu1 = 0
                else:
                    r = r1
if k <= 0 and r > 0:#pontuação paa saber quem ganhou o round
    pr = 1
    pk = 0
else:
    pk = 1
    pr = 0
#segundo round
r = 50
k = 50
p = int(input())
acu = 0
acu1 = 0
k1 = 1
r1 = 1
while k > 0 and r > 0:
    ki = k
    ri = r
    if k1 <= 0 or r1 <= 0:
        break
    else:
        while p > 0:#situação dos numeros positivos
            acu = acu + p
            k1 = k - p
            if k1 <= 0:
                print ("Ken:" ,ki, "-" ,acu, "=" ,k1)#ken derrotado
                k = k1
                break
            else:
                p = int(input())
                if p < 0 or k1 <= 0:
                    print ("Ken:" ,ki, "-" ,acu, "=" ,k1)
                    k = k1
                    acu = 0
                    break
                else:
                    k = k1
        while p < 0:#situação dos numeros negativos
            acu1 = acu1 - p
            r1 = r + p
            if r1 <= 0:
                print("Ryu:" , ri, "-" ,acu1, "=" ,r1)#ryu derrotado
                r = r1
                break
            else:
                p = int(input())
                if p > 0 or r1 <= 0:
                    print("Ryu:" , ri, "-" ,acu1, "=" ,r1)
                    r = r1
                    acu1 = 0
                else:
                    r = r1
if k <=0 and r > 0:#pontuação do segundo round
    pr1 = 1
    pk1 = 0
else:
    pk1 = 1
    pr1 = 0
if pr + pr1 == 2:#calculo para ver quem vnceu ou se empatou
    print ("Ryu venceu")
elif pk + pk1 == 2:
    print ("Ken venceu")
else:
    print("empatou")
        
