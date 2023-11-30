
def validar (nota=0):
    validas = 0
    media = 0
    while validas < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            media += nota
            validas += 1
    return media/2

def main():
    print(f'media = {validar():.2f}')


if __name__ == "__main__":
    main()