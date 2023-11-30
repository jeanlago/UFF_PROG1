
linhas = int(input())

for i in range ((linhas*4)+1):
    if i !=0 and i % 4 == 0:
        print('PUM')
    elif i != 0:
        print(f"{i} ", end="")
