
def precos(item=0,quantidade=0):
    if item ==1:
        return 4.00 * quantidade
    elif item == 2:
        return 4.50 * quantidade
    elif item == 3:
        return 5.00 * quantidade
    elif item == 4:
        return 2.00 * quantidade
    elif item == 5:
        return 1.50 * quantidade

def main():
    item, quantidade = (map(int,input().split()))
    print(f'Total: R$ {precos(item,quantidade):.2f}')

if __name__ == '__main__':
    main()
