
def main():
    C = int(input())

    for i in range(C):
        palavra = input()
        segundos = len(palavra) / 100
        print(f'{segundos:.2f}')

if __name__ == '__main__':
    main()
