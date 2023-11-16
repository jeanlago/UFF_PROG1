from math import log

def rosser(n=0):
    logden = (n/log(n))
    return 1.25506 * logden


def main():
    n = float(input())

    #printando P e depois M
    print(f'{n/log(n):.1f} ', end='')
    print(f'{rosser(n):.1f}')


if __name__ == '__main__':
    main()
