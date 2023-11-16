

def menorpossivi(n=0):
    cem,cinquenta,vinte,dez,cinco,dois,um = [0] * 7

    while n > 0:
        if n - 100 >= 0:
            cem += 1
            n -= 100
        elif n - 50 >= 0:
            cinquenta += 1
            n -= 50
        elif n - 20 >= 0:
            vinte += 1
            n -= 20
        elif n - 10 >= 0:
            dez += 1
            n -= 10
        elif n - 5 >= 0:
            cinco += 1
            n -= 5
        elif n - 2 >= 0:
            dois += 1
            n -= 2
        elif n - 1 >= 0:
            um += 1
            n -= 1
    return cem, cinquenta, vinte, dez, cinco, dois, um

def main():
    N = int(input())
    lista= menorpossivi(N)
    print(f'{N}\n{lista[0]} nota(s) de R$ 100,00\n{lista[1]} ',end='')
    print(f'nota(s) de R$ 50,00\n{lista[2]} nota(s) de R$ 20,00')
    print(f'{lista[3]} nota(s) de R$ 10,00\n{lista[4]} nota(s) de R$ 5,00')
    print(f'{lista[5]} nota(s) de R$ 2,00\n{lista[6]} nota(s) de R$ 1,00')



if __name__ == '__main__':
    main()
