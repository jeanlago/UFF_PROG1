

def main():
    decimal = int(input())

    hexadecimal = lambda numero: hex(numero)[2:].upper()
    print(hexadecimal(decimal))

if __name__ == "__main__":
    main()
