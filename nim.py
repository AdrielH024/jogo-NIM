#nim novo


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    dadosescolhidos = False
    while(dadosescolhidos == False):
        if(n <= 0 or m == 0 or m > n):
            print("erro")
        else:
            if(n % (m+1) != 0):
                p = 2
                print("Computador começa!")
                dadosescolhidos = True
            else:
                print("Você começa!")
                p=1
                dadosescolhidos = True
    while(n > 0):
        if(p == 2):
            print("Vez do computador!")
            n = n - computador_escolhe_jogada(n,m)
            if(n == 0):
                break
            p = 1
        if(p ==1 ):
            print("Sua vez!")
            n = n - usuario_escolhe_jogada(n,m)
            if(n == 0):
                break
            p = 2
    if(p == 1):
        print("você ganhou")
    if(p == 2):
        print ("Fim do jogo! O computador ganhou!")
        
def campeonato():
    vm = 3
    vp = 0

    i = 1
    while(i <= 3):
       print("**** ,Rodada ", i," ****") 
       partida()
       i = i + 1

    print("**** Final do campeonato! ****")
    print("Placar: Você",vp, " X ", vc, "Computador")

def computador_escolhe_jogada(n,m):
    a =m
    if(n - m > 0):
        while((n-a) % (m+1) != 0):
            a = a-1
        m=a
        print("O computador tirou ",m, " peças")
        n = n-m
        print("faltam ", n, "peças no tabuleiro")  
    elif(n-m < 0 or n-m == 0):
        m = n 
        n = 0
        if( m > 1):
            print("O computador tirou ",m, " peças")
        elif(m == 1):
               print("O computador tirou uma peça")
        if(n > 1):
            print("faltam ", n, "peças no tabuleiro") 
        elif(n ==1):
            print ("Agora resta apenas uma peça no tabuleiro.")
    return m


def usuario_escolhe_jogada(n,m):
    fezjogada=False
    while(fezjogada == False):
        a = int(input("Quantas peças você vai tirar? "))
        if(a <= 0 or a > m or n - a < 0):
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            if(a > 1):
                print("Você tirou ",a," peças")
            elif(a ==1):
                print("Voce tirou uma peça")
            n = n - a
            if(n > 1):
                print("faltam ", n, "peças no tabuleiro")
            elif(n == 1):
                ("Agora resta apenas uma peça no tabuleiro.")
            fezjogada = True
    return a

def main():
    
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    n = int(input())
    if(n == 1):
        partida()
        print ("Voce escolheu uma partida isolada")
    if(n == 2):
        print ("Voce escolheu um campeonato!")
        campeonato()


main()