
def main():
    lista = list(map(int,input().split()))

    calcular_hora_chegada = lambda lista: (lista[0] + lista[1] + lista[2]) % 24

    print(calcular_hora_chegada(lista))


if __name__ == '__main__':
    main()