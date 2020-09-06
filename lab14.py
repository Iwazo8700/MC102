#Daniel Mendes dos Santos
#ra214752
#Comentario
def ord(lista):
    p = 0
    for i in range(len(lista)-2): #ornedado decrescente
        if lista[i]>lista[i+1]:
            p=2
        else:
            p=0
            break
    if p!=2:
        for i in range(len(lista)-2): #ornedado crescente
            if lista[i]<lista[i+1]:
                p=1
            else:
                p=0
                break
    return p

def imprimir(lista):                  
    if len(lista)>=0:                    
        for i in range(len(lista)):       
            print(lista[i], end=' ')
        print()    

def ordenard(lista): #ordena crescente
    for b in range(len(lista)):
        for a in range(len(lista)-1):
            if lista[a]<lista[a+1]:
                aux = lista[a]
                lista[a] = lista[a+1]
                lista[a+1]= aux

def ordenarc(lista):#ordena decrescente
    for b in range(len(lista)):
        for a in range(len(lista)-1):
            if lista[a]>lista[a+1]:
                aux = lista[a]
                lista[a] = lista[a+1]
                lista[a+1]= aux


def buscabinaria (lista,procurado):
    passos=[]
    inicio =0
    fim=len(lista)- 1
    k= ord(lista)
    flag3 = 1

    if k==1: #crescente
        while inicio <= fim:
            meio = (inicio+fim )//2
            print(meio, end=' ')
            if lista [meio] == procurado:
                print('\n%d esta na posicao: %d' %(procurado, meio))
                flag3 = 0
                break
            elif lista[meio]>procurado:
                fim = meio-1
            else:
                inicio = meio + 1

    if k==2: #decrecente
        while inicio <= fim:
            meio = (inicio+fim )//2
            print(meio, end=' ')
            if lista [meio] == procurado:
                print('\n%d esta na posicao: %d' %(procurado, meio))
                flag3 = 0
                break
            elif lista[meio]>procurado:
                inicio = meio + 1
            else:
                fim = meio-1

    if k==0:#desordenado
        print("Vetor nao ordenado!")
            
    if flag3==1:
        print("\n%d nao esta na lista!" % (procurado))




def inserir(lista,ra):
    k= ord(lista)
    if k==1:#crescente
        posicao = len(lista)                
        for i in range(len(lista)): 
            if lista[i] > ra:
                posicao = i     
                break       
        lista.insert(posicao,ra)
        return lista 
    if k==2:#decrescente
        posicao = len(lista)                
        for i in range(len(lista)): 
            if lista[i] < ra:
                posicao = i     
                break       
        lista.insert(posicao,ra) 
        return lista
    if k==0:#desordenado
        nova= lista+[ra]
        return nova

def remover(lista,ra):
        for i in range(len(lista)):
            if lista[i] == ra :
                jooj=lista[0:i]+lista[i+1:len(lista)]
                return jooj
        return lista




entrada = input()
ras = [int(i) for i in entrada.split()]


while(1):
    entrada2=input()
    dest=[str(i) for i in entrada2.split()]
    acao= dest[0]
    if len(dest)==2:
        raentrando=int(dest[1])
    if acao== 'p':
        imprimir(ras)
    if acao== 'c':
        ordenarc(ras)
    if acao== 'd':
        ordenard(ras)

    if acao== 'b':
        buscabinaria(ras,raentrando)


    if acao== 'i':
        flag2=0
        for i in range(len(ras)):
            if raentrando == ras[i]:
                print("Aluno ja matriculado na turma!")
                flag2=1
        if flag2==0:
            if len(ras)==150:
                print("Limite de vagas excedido!")
            else:
               ras=inserir(ras,raentrando)
        flag2=0
    if acao== 'r':
        if (len(ras)) == 0:
            print("Nao ha alunos cadastrados na turma!")
        else:
            flag1=0
            for i in ras:
                if i == raentrando:
                    flag1=1
            if flag1==1:
                ras=remover(ras,raentrando)
            if flag1==0:
                print("Aluno nao matriculado na turma!")
        flag1=0
    if acao== 's':
        break


