def modulo(a, b):
    m = a % b

    if m < 0:
        m = m - b if b < 0 else m + b

    return m

def main():
    a, b = map(int, input().split())

    r = modulo(a, b)
    d = (a - r) // b
    print(f'{d} {r}')

if __name__ == '__main__':
    main()
