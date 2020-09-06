#nome: Enzo Hideki Iwata    RA:215394
n = int(input())#dias
acao1 = []
acao2 = []
acao3 = []
acao4 = []
lucrof = 0.0
c1 = 0
v1 = 0
c2 = 0
v2 = 0
c3 = 0
v3 = 0
c4 = 0
v4 = 0
acu1 = 0
acu2 = 0
acu3 = 0
acu4 = 0
for i in range(n):#lista para cada ação
    custo = float(input())
    acao1.append(custo)
for i in range(n):
    custo = float(input())
    acao2.append(custo)
for i in range(n):
    custo = float(input())
    acao3.append(custo)
for i in range(n):
    custo = float(input())
    acao4.append(custo)
if n == 2:#para dois dias entra nesse if
    for a in range(n-1):
        res1 = acao1[1] - acao1[0]
        res2 = acao2[1] - acao2[0]
        res3 = acao3[1] - acao3[0]
        res4 = acao4[1] - acao4[0]
        qwert = max(res1, res2, res3, res4)
        if qwert == res1:
            print("acao1: compra 1, venda 2, lucro","%.2f"%qwert)
        if qwert == res2:
            print("acao2: compra 1, venda 2, lucro","%.2f"%qwert)
        if qwert == res3:
            print("acao3: compra 1, venda 2, lucro","%.2f"%qwert)
        if qwert == res4:
            print("acao4: compra 1, venda 2, lucro","%.2f"%qwert)
else:#faz todas as combinações possiveis
    for compra1 in range(n):
        for venda1 in range(compra1, n):
            for compra2 in range(n):
                for venda2 in range(compra2, n):
                    for compra3 in range(n):
                        for venda3 in range(compra3, n):
                            for compra4 in range(n):
                                for venda4 in range(compra4, n):
                                    luc1 = acao1[venda1] - acao1[compra1]#da o lucro para cada situação de cada ação separadamente
                                    luc2 = acao2[venda2] - acao2[compra2]
                                    luc3 = acao3[venda3] - acao3[compra3]
                                    luc4 = acao4[venda4] - acao4[compra4]
                                    av = True
                                    if compra1 == venda1:#caso o dia de compra e o de venda sejam as mesmas entra-se no if( significa que tal acao nao foi comprada)
                                        co1 = 17
                                        ve1 = 18
                                    else:
                                        co1 = compra1
                                        ve1 = venda1
                                    if compra2 == venda2:
                                        co2 = 19
                                        ve2 = 20
                                    else:
                                        co2 = compra2
                                        ve2 = venda2
                                    if compra3 == venda3:
                                        co3 = 21
                                        ve3 = 22
                                    else:
                                        co3 = compra3
                                        ve3 = venda3
                                    if compra4 == venda4:
                                        co4 = 23
                                        ve4 = 24
                                    else:
                                        co4 = compra4
                                        ve4 = venda4
                                        #ifs de verificação
                                    if (co1==co2)or(co1==co3)or(co1==co4)or(co2==co3)or(co2==co4)or(co3==co4)or(ve1==ve2)or(ve1==ve3)or(ve1==ve4)or(ve2==ve3)or(ve2==ve4)or(ve3==ve4):
                                        av = False
                                    if (co1>co2 and co1<ve2)or(co1>co3 and co1<ve3)or(co1>co4 and co1<ve4)or(co2>co1 and co2<ve1)or(co2>co3 and co2<ve3)or(co2>co4 and co2<ve4)or(co3>co2 and co3<ve2)or(co3>co1 and co3<ve1)or(co3>co4 and co3<ve4)or(co4>co2 and co4<ve2)or(co4>co3 and co4<ve3)or(co4>co1 and co4<ve1):
                                        av = False
                                    if (ve1>co2 and ve1<ve2)or(ve1>co3 and ve1<ve3)or(ve1>co4 and ve1<ve4)or(ve2>co1 and ve2<ve1)or(ve2>co3 and ve2<ve3)or(ve2>co4 and ve2<ve4)or(ve3>co2 and ve3<ve2)or(ve3>co1 and ve3<ve1)or(ve3>co4 and ve3<ve4)or(ve4>co2 and ve4<ve2)or(ve4>co3 and ve4<ve3)or(ve4>co1 and ve4<ve1):
                                        av = False
                                    if av:
                                        lucf = luc1 + luc2 + luc3 + luc4
                                        if lucf > lucrof:#acumulador do maior lucro e dos dados desse lucro
                                            lucrof = lucf
                                            c1 = compra1 + 1
                                            c2 = compra2 + 1
                                            c3 = compra3 + 1
                                            c4 = compra4 + 1
                                            v1 = venda1 + 1
                                            v2 = venda2 + 1
                                            v3 = venda3 + 1
                                            v4 = venda4 + 1
                                            acu1 = round(luc1, 2)
                                            acu2 = round(luc2, 2)
                                            acu3 = round(luc3, 2)
                                            acu4 = round(luc4, 2)
                                            lucrof = round(lucrof, 2)
if c1 != v1:
    print("acao 1: compra %d,"%c1,"venda %d,"%v1,"lucro %.2f"%acu1)
if c2 != v2:
    print("acao 2: compra %d,"%c2,"venda %d,"%v2,"lucro %.2f"%acu2)
if c3 != v3:
    print("acao 3: compra %d,"%c3,"venda %d,"%v3,"lucro %.2f"%acu3)
if c4 != v4:
    print("acao 4: compra %d,"%c4,"venda %d,"%v4,"lucro %.2f"%acu4)
print("Lucro: %.2f"%lucrof)
