
MERCADOS = int(input())

minimo = float('inf')

for i in range(MERCADOS):
    preco, gramas = map(float, input().split())
    preco_por_grama = (preco / gramas)
    if preco_por_grama < minimo:
        minimo = preco_por_grama

total = minimo * 1000

print(f"{total:.2f}")
