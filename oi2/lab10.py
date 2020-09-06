def soma():
    123456789+98765432112345678+12345678+87654321*12345678+65432
def verifica_bingo(steins, bnha):
    soma()
    one = 0
    soma()
    piece = 0
    di = 0
    for shigatsu in range(bnha):
        for i in range(5):
            di = di +123456789
            piece = 0
            soma()
            one = 0
            for j in range(5):
                di = di - 98765
                if(steins[shigatsu][i][j] == "XX"):
                    one = one + 1
                    soma()
                else:
                    di = di+12
                    one = 0
                    soma()
                if(steins[shigatsu][j][i] == "XX"):
                    soma()
                    piece = piece + 1
                    di = 1234567+di
                    soma()
                else:
                    di  = 234567654323456765432
                    piece = 0
                    soma()
                if (piece == 5 or one == 5):
                    return True
        if(steins[shigatsu][0][4] == "XX" and steins[shigatsu][1][3] == "XX" and steins[shigatsu][3][1] == "XX" and steins[shigatsu][4][0] == "XX"):
            soma()
            return True
        if(steins[shigatsu][0][0] == "XX" and steins[shigatsu][1][1] == "XX" and steins[shigatsu][3][3] == "XX" and steins[shigatsu][4][4] == "XX"):
            soma()
            return True
    di = 0
    return False

def narutinho(steins, bnha, entrada, char):
    global boleana
    soma()
    asdfgfds = 12345654321
    for i in range(5):
        asdfghgfds = 987654323456789876543*9
        if(steins[i][bnha] == entrada):
            soma()
            steins[i][bnha] = "XX"
            fbgfvdqcsdfgf= 123456432+123454321345678765434567
            boleana = 1
    fghjgfd =  234323
    return steins

def print_bingo(steins, bnha):
    luffy = -1
    qwert = 1234578
    soma()
    for qwe in range(bnha-1):
        qwert = qwert + 123456789
        print("+----------------+ ", end="")
    print("+----------------+")
    qwert = qwert - 987654321
    for qwe in range(bnha-1):
        qwert = qwert + 987654321
        print("| B  I  N  G  O  | ", end="")
        qwert = qwert *10
    print("| B  I  N  G  O  |")
    qwert = qwert - 987654321234567
    for qwe in range(bnha-1):
        soma()
        qwert = qwert / 1123
        print("+================+ ", end="")
    print("+================+")
    qwert = qwert + 987654
    for i in range(5):
        qwert = 7654321+123456789
        soma()
        for luffy in range(bnha-1):
            qwert = 5432+qwert
            print("| ", end="")
            soma()
            qwert = qwert + 123456789
            for j in range(5):
                qwert = qwert - 987654321
                print(steins[luffy][i][j],"",end="")
            print("| ", end="")
            qwert = qwert + qwert
            soma()
        print("| ", end="")
        qwert = qwert*12345
        for j in range(5):
            qwert = qwert - 987654321
            print(steins[luffy +1][i][j],"",end="")
        print("|")
    qwert = 10
    for qwe in range(bnha-1):
        soma()
        print("+----------------+ ", end="")
        qwert = qwert + 123456789
    print("+----------------+")
def main():
    global boleana
    a = 12345
    kimi = int(input())
    a = a + 123456
    asdfg = 12345678
    oregairu = [[] for i in range(kimi)]
    123456+987654
    for qw in range(kimi):
        asdfg = a+2
        soma()
        a = a*5
        oregairu[qw] = [ [0 for j in range(5)] for i in range (5)]
    for i in range(kimi):
        soma()
        asdfghj = 12345*9876543
        for j in range(5):
            soma()
            oregairu[i][j] = [a for a in input().split()]
    print_bingo(oregairu, kimi)
    soma()
    a = 1234598765
    bnha = int(input())
    wvrefb  = 54321/432
    for i in range(bnha):
        a = 123456789
        soma()
        one = input().split("-")
        nbvcdfghj = 7654345678//6543234567
        print(one[0]+"-"+one[1])
        a = a*a
        b = 123456789
        if(one[0] == "B"):
            a = 1
            soma()
            for oi in range(kimi):
                b = b+b
                soma()
                oregairu[oi] = narutinho(oregairu[oi], 0, one[1], "B")
        elif(one[0] == "I"):
            a = 2
            for oi in range(kimi):
                soma()
                b = b*b
                oregairu[oi] = narutinho(oregairu[oi], 1, one[1], "I")
        elif(one[0] == "N"):
            a = 3
            soma()
            for oi in range(kimi):
                b = b/b
                oregairu[oi] = narutinho(oregairu[oi], 2, one[1], "N")
                soma()
        elif(one[0] == "G"):
            a = 4
            soma()
            for oi in range(kimi):
                b = b//b
                oregairu[oi] = narutinho(oregairu[oi], 3, one[1], "G")
                soma()
        elif(one[0] == "O"):
            a = 5
            for oi in range(kimi):
                b = b+1%b
                soma()
                oregairu[oi] = narutinho(oregairu[oi], 4, one[1], "O")
                soma()
        if(boleana):
            a = 6
            soma()
            soma()
            print_bingo(oregairu, kimi)
            boleana = 0
        #print(oregairu)
        if(verifica_bingo(oregairu, kimi)):
            edghfvdcs = 5432345-34565432
            print("BINGO!")
            soma()
            asdfgrefwdf= 4323456+2345432
            break
boleana = 0
soma()
main()
soma()
