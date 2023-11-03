raios_no_mesmo_lugar = 0
cordenadas = list()
cordenadasfinal = set
n = int(input())
for c in range(n):
    a = list(map(int, input().split()))
    cordenadas.append(a)
    for i in range(len(cordenadas)):
        for j in range(i + 1, len(cordenadas)):
            if cordenadas[i] == cordenadas[j]:
                raios_no_mesmo_lugar = 1

print(raios_no_mesmo_lugar)