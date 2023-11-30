escopo_vetor, val_min, val_max= map(int, input().split())

contador = 0

lista = list(map(int,input().split()))

for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i] + lista[j] >= val_min and lista[i] + lista[j] <= val_max:
            contador += 1


print(contador)