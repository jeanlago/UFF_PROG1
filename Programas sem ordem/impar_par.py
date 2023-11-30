
Jogo = int(input())
partida = 0
vez = 0
while Jogo != 0:
    vencedor = []
    jogador1 = str(input())
    jogador2 = str(input())
    while vez < Jogo:
        val1, val2 = map(int,(input().split()))

        if (val1 + val2) %2 == 0:
            vencedor.append(jogador1)
        else:
            vencedor.append(jogador2)
        vez += 1
    partida += 1
    print(f"Teste {partida}")
    for valor in vencedor:
        print(valor)
    print()
    Jogo = int(input())
    vez = 0
