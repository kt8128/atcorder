from bisect import bisect

n, k = map(int, input().split())
*v, = map(int, input().split())
candidate = []
for i in range(k+1):
    for j in range(k-i+1):
        if i + j >= n:
            candidate.append(v)
        elif j == 0:
            candidate.append(v[:i])
        else:
            candidate.append(v[:i]+v[(-1)*j:])
ans = 0
for cand in candidate:
    cand.sort()
    idx = bisect(cand, -1)
    rem = k-len(cand)
    p = min(idx, rem)
    if ans < sum(cand[p:]):
        a = cand
        b = p
        ans = sum(cand[p:])
print(ans)
