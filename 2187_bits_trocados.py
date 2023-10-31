contador = 0
teste = 1

while teste != 0:
    contador += 1
    valor = float(input())
    if valor == 0:
        break

    I, J, K, L = 0, 0, 0, 0  # Zerando as contagens para cada conjunto de teste

    while valor != 0:
        if valor - 50 >= 0:
            I += 1
            valor -= 50
        elif valor - 10 >= 0:
            J += 1
            valor -= 10
        elif valor - 5 >= 0:
            K += 1
            valor -= 5
        elif valor - 1 >= 0:
            L += 1
            valor -= 1

    print(f"Teste {contador}")
    print(f"{I} {J} {K} {L}\n")
