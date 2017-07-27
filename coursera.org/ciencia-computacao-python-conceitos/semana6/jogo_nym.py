import time

def sorteia_jogador():
    ms = time.time()*1000.0
    return (ms % 2 == 0)
    
def computador_escolhe_jogada(n, m):
    jogadas = range(1, m)
    jogada = 1
    
    multiplicador = m + 1
    for i in jogadas:
        restante = n - i
        if(restante % multiplicador == 0):
            jogada = i
            break
        
    if(jogada == 1):
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou {} peças.".format( jogada ))
    return jogada

def usuario_escolhe_jogada(n, m):
    while(True):
        jogada = int(input("Quantas peças você vai tirar?"))
        if(jogada > n | jogada > m):
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            break;
    if(jogada == 1):
        print("Você tirou uma peça.")
    else:
        print("Você tirou {} peças.".format( jogada ))
    return jogada

def status_tabuleiro(n):    
    if(n == 1):
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam {} peças no tabuleiro".format( n ))
            
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    jogador = sorteia_jogador()

    if(jogador):
        print("\nVocê começa!\n")
    else:
        print("\nComputador começa!\n")

    while True:
        if(jogador):
            jogada = usuario_escolhe_jogada(n, m)
        else:
            jogada = computador_escolhe_jogada(n, m)
        n = n - jogada
        if(n > 0):
            status_tabuleiro(n)
        else:
            print("Fim do jogo! ")
            if(jogador):
                print ("Você ganhou!")
                return True
            else:
                print ("O computador ganhou!")
                return False
        jogador = not jogador
           
def campeonato():
    partidas = 0
    vitoriasJogador = 0
    vitoriasComputador = 0
    for x in range(0, 3):
        vencedor = partida()
        if(vencedor):
            vitoriasJogador = vitoriasJogador + 1
        else:
            vitoriasComputador = vitoriasComputador + 1

    print("**** Final do campeonato! ****\n\n")
    print("Placar: Você {} X {} Computador\n".format( vitoriasJogador, vitoriasComputador ))
    return

print("Bem-vindo ao jogo de NIM! Escolha:\n\n")
print("1 - para jogar uma partida isolada\n")
opcao = int(input("2 - para jogar um campeonato\n"))

if(opcao == 1):
    print("\nVocê escolheu uma partida!\n")
    partida()
else:
    print("\nVocê escolheu um campeonato!\n")
    campeonato()

