
def main():
    lista = list(map(int,input().split()))

    perimetro = lambda valores: valores[0] * valores[1]

    print(perimetro(lista))

if __name__ == '__main__':
    main()
