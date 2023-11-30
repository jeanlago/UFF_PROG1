from math import sqrt

def fibonnas(n=0):
    return (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5)

def main():
    n = int(input())
    print(f'{fibonnas(n):.1f}')


if __name__ == '__main__':
    main()