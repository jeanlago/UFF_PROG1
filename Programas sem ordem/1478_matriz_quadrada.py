
def construir_matriz(ordem):
    matriz = []
    for i in range(1, ordem + 1):
        linha = []
        for j in range(1, ordem + 1):
            linha.append(abs(i - j) + 1)
        matriz.append(linha)
    for linha in matriz:
        print(" ".join(map(lambda x: f"{x:3}", linha)))

    print()

def main():
    ordem = int(input())
    while ordem != 0:
        construir_matriz(ordem)
        ordem = int(input())

if __name__ == '__main__':
    main()
