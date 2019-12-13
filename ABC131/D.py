n = int(input())
AB = [list(map(int, input().split())) for i in range(n)]
AB.sort(key=lambda x: x[1])
now = 0
for a, b in AB:
    now += a
    if now > b:
        print('No')
        exit()
print('Yes')
