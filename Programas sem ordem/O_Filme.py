
def main():
    lista = list(map(float,input().split()))

    subiu = lambda valores: ((valores[1]-valores[0])/valores[0])*100

    print(f'{subiu(lista):.2f}%')

if __name__ == '__main__':
    main()
