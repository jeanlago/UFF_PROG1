
x = int(input())

while x != 0:
    for i in range(1,x+1):
        if i < x:
            print(f"{i} ", end='')
        else:
            print(f"{i}", end='')
            print()
    x = int(input())
