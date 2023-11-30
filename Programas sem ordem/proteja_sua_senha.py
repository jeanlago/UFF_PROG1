# Função para encontrar a senha com base nas associações entre letras e números
def encontrar_senha(associacoes):
    senha = ""
    for i in range(len(associacoes[0]) // 2):
        for j in range(len(associacoes)):
            senha += associacoes[j][i * 2:i * 2 + 2][associacoes[j].index(associacoes[j][-1])]
    return senha

# Variável para contar os testes
teste = 1

while True:
    N = int(input())  # Número de associações entre letras e números

    if N == 0:
        break  # Condição de saída

    # Armazenamento das associações entre letras e números
    associacoes = []
    for _ in range(N):
        entrada = input().split()
        associacoes.append(entrada)

    # Encontrar a senha do cliente
    senha_cliente = encontrar_senha(associacoes)

    # Impressão dos resultados para o conjunto de teste atual
    print(f"Teste {teste}")
    print(' '.join(senha_cliente))
    print()  # Linha em branco entre os conjuntos de teste
    teste += 1
