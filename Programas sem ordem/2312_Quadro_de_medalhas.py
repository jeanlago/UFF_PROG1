
def main():
    N = int(input())
    paises = []

    for i in range(N):
        linha = input().strip().split()
        nome = linha[0]
        valores = list(map(int, linha[1:]))
        linha_convertida = [nome] + valores
        paises.append(linha_convertida)

    minha_chave= lambda lista: (-lista[1], -lista[2], -lista[3], lista[0])
    paises.sort(key=minha_chave)

    for i in range(len(paises)):
        for j in range(4):
            print(f'{paises[i][j]}', end='')
            if j < 3:
                print(' ', end='')
        print()

if __name__ == "__main__":
    main()