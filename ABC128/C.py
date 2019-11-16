import numpy as np

n, m = map(int, input().split())
S = []
for _ in range(m):
    *a, = map(int, input().split())
    l = a[1:]
    S.append(l)
*p, = map(int, input().split())

ans = 0
for i in range(2**n):
    tmp = np.array([i >> j & 1 for j in range(n)])
    if p == [sum(tmp[np.array(s)-1]) % 2 for s in S]:
        ans += 1
print(ans)
