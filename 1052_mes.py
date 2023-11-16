
def mes(N=0):
    lista = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return lista[N-1]


def main():
    N = int(input())
    print(mes(N))

if __name__ == "__main__":
    main()
