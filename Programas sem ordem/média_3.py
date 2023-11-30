
def ponderada(N1, N2, N3, N4):
    media = ((N1*2) + (N2*3) + (N3*4) + (N4*1))/10
    return(media)

valores_float = list(map(float, input().split()))
media = ponderada(*valores_float)

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")

elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")

else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    media_final = float(input())
    print(f'Nota do exame: {media_final}')
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    media_final = (media_final + media)/2
    print(f'Media final: {media_final:.1f}')
