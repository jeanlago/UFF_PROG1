
N = int(input())
for i in range(N):
    val1, val2 = input().split()
    if len(val2) <= len(val1):
        # A captura dos últimos quatro dígitos de val1
        last_four_val1 = val1[-len(val2):]

        # Comparação com val2
        if last_four_val1 == val2:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
