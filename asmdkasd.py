#entrada: n teste, nomes e numeros inseridos pelos jogadores
#saida: numero do teste da partida, e ganhadores de cada uma

#partidas são "consideradas" a partir da 1
id = 1
#LAÇO DE REPETIÇÃO DO Nº DE PARTIDAS COM CRITÉRIO DE PARADA = 0
while True:
    lista_ganhadores =[]
    n=int(input())
    if (n == 0):
        break

    #recebe nome dos jogadores
    jog1 = int(input())
    jog2 = int(input())

    #laço que roda n vezes, define ganhador das partidas e
    # armazena ganhadores na lista
    for i in range(n):
        a,b=map(int,input().split())

        if((a+b)%2==0):
            lista_ganhadores.append(jog1)
        else:
            lista_ganhadores.append(jog2)

    #imprime numeração do teste
    print(f"Teste {id}")

    #laço que vai percorrer a lista e printar ganhadores
    for i in range(len(lista_ganhadores)):
        print(lista_ganhadores[i])
    #
    print()
    id+=1