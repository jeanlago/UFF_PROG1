
def main():
    base, altura, raio= map(float, input().split())

    print(f'TRIANGULO: {base*raio/2:.3f}')
    print(f'CIRCULO: {raio**2 *3.14159:.3f}')
    print(f'TRAPEZIO: {((base+altura)*raio)/2:.3f}')
    print(f'QUADRADO: {(altura**2):.3f}')
    print(f'RETANGULO: {base*altura:.3f}')


if __name__ == '__main__':
    main()
