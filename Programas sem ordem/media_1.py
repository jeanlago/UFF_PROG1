
def main():

    x = float(input())
    y = float(input())

    soma = lambda x, y: (x*3.5 + y*7.5)/11

    print(f'MEDIA = {soma(x, y):.5f}')
if __name__ == '__main__':
    main()
