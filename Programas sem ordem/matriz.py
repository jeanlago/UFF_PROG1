# Inicialize uma matriz vazia
matriz = []

# Crie a matriz 6x6 com valores das colunas
for i in range(7):
    linha = []  # Inicialize uma nova linha vazia para cada iteração externa
    for j in range(7):
        linha.append(j)  # Adicione o valor da coluna (j) à linha atual
    matriz.append(linha)  # Adicione a linha à matriz

# Imprima a matriz
for linha in matriz:
    print(linha)
