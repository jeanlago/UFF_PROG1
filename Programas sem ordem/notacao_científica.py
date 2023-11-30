def formatar_notacao_cientifica(numero):
    formato = "{:+.4e}".format(numero)
    parte_inteira, parte_decimal = formato.split('e')
    return f"{parte_inteira}E{parte_decimal[0]}{parte_decimal[1:3]}"

def main():
    numero_ponto_flutuante = float(input())
    resultado_notacao_cientifica = formatar_notacao_cientifica(numero_ponto_flutuante)
    print(resultado_notacao_cientifica)

if __name__ == "__main__":
    main()
