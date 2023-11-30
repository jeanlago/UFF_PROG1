'''função para verificar se a matriz quadrada calcula a transposta (se B é a matriz transposta de A então aij==bji)'''

def transposta(M):
    M_t = list(map(list, zip(*M)))

    return M_t

matriz = []

N = int(input("Digite a ordem da matriz: "))

for i in range(N):
    matriz_filha = []
    for j in range(N):
        matriz_filha.append(int(input(f'Digite um valor para a posição ({i},{j}): ')))
    matriz.append(matriz_filha)

print(transposta(matriz))