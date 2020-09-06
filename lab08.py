#nome: Enzo Hideki Iwata    RA:215394
#O programa fará uma previsão do PCf de determinado monstro após a sua evolução, isso acontecerá pela analise de um banco de dados fornecido préviamente e calculará a media do valor multiplicador de cada pokemon e assim prever o Pc do pokemon após a evolução
n = int(input())#quantidade de pokemon a serem analisados
lista = [[] for ghj in range(0, 1000)]#lista dos indicadores
acu = 0
for a in range (n):
    linha = input()
    ints = [int(i) for i in linha.split( )]
    indf = ints[0]
    PCa = ints[1]
    PCf = ints[2]
    ind = indf - 1#definições de CPa, CPf e indentificador para o banco de dados
    x = lista[ind]#para cada valor do indentificador de entrada há um correspondente na lista 1
    multi = float(PCf/PCa)#multiplicador da especie especifica
    #5 casas apos a divisão
    x.append(multi)#insere o dado do multiplicador na lista na posição do ind
pot = len(lista)
for num in range(pot):#num pega todos valores para a lista
    tal = lista[num]#tal vira a lista composta por todos os multiplicadores de um id
    if tal != []:
        port = len(tal)
        for kak in range(port):#pego cada valor do multi e coloco e kak
            zet = float(tal[kak])
            acu = acu + zet#faço a acumuladora de todos alores para multi encontardos
        multif = float(acu/(port))#media final de determinado id
        lista[num] = multif
        acu = 0
linha2 = input()#parte das evoluções
while n != 0:
    ints2 = [int(j) for j in linha2.split( )]#entradas com dois numeros
    indf2 = ints2[0]
    PCa2 = ints2[1]
    if PCa2 == 0 or indf2 == 0:#se os dois numeros forem 0 então o programa acaba
        break
    ind2 = indf2 - 1
    c =  float(lista[ind2])
    PCf2 = c*PCa2#multiplicação e resultado final
    #arredondando para um inteiro o resultado final
    PCf2 = int(PCf2)
    PCf2 = PCf2 +1
    print(PCf2)
    linha2 = input()
