
lista = []
for i in range(3):
    lista[i] = int(input(""))

DELTA = lista[2] - 4*lista[1]*lista[3]

X1 = (-lista[2] +DELTA) /(2*lista[1])
X2 = (-lista[2] -DELTA) / (2*lista[1])

print(f"{X1} {X2}")
