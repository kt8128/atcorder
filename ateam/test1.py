n = int(input())
P = list(map(int, input().split()))
ans = P[0]
m = P[0]
for p in P[1:]:
    if p >= m:
        ans += m
    else:
        ans += p
        m = p
print(ans)
