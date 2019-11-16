n = int(input())
*P, = map(int, input().split())
cnt = 0
for i, p in enumerate(P):
    if i + 1 != p:
        cnt += 1
if cnt <= 2:
    print('YES')
else:
    print('NO')
