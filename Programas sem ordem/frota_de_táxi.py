ALCOOL, GASOLINA, REND_ALC, REND_GAS= map(float, input().split())


preco_alc = ALCOOL / REND_ALC
preco_gas = GASOLINA / REND_GAS

if preco_alc < preco_gas:
    print("A")
else:
    print("G")
