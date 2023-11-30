
def main():
    val1, val2, val3 = map(int,input().split())

    maior = lambda a, b, c: a if a > b and a > c else b if b > c else c

    print(f'{maior(val1,val2,val3)} eh o maior')


if __name__ == "__main__":
    main()