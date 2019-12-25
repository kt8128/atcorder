n, m = map(int, input().split())
S = []
for _ in range(m):
    S.append(list(map(int, input().split()))[1:])
*p, = map(int, input().split())

ans = 0
for i in range(2**n):
    switch = [i >> j & 1 for j in range(n)]
    c = 0
    for k, s in enumerate(S):
        count = 0
        for s1 in s:
            if switch[s1-1]:
                count += 1
        if count % 2 == p[k]:
            c += 1
    if m == c:
        ans += 1
print(ans)
