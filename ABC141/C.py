n, k, q = map(int, input().split())
point = [0] * n
for _ in range(q):
    a = int(input())
    point[a-1] += 1

ans = [k] * n
for i, p in enumerate(point):
    ans[i] -= q - p

for a in ans:
    if a > 0:
        print('Yes')
    else:
        print('No')
