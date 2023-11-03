n = int(input())
v1 = int(input())
ac = 1

while n > 1:
    n -= 1
    v2 = int(input())
    if v2 != v1:
        ac += 1
        v1 = v2

print(ac)
