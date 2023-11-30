N, C = map(int, input().split())
cotacoes = list(map(int, input().split()))

lucro = 0

for i in range(1, N):
    if cotacoes[i] <= (cotacoes[i - 1] + C):
        continue  # Se o preço diminuir, não faz sentido vender, seguimos para o próximo dia
    else:
        lucro += min(cotacoes[i] - cotacoes[i - 1], C)  #Lucro será a menor diferença ou a taxa de corretagem

print(lucro)
