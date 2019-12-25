import heapq

n, k = map(int, input().split())
S = input()
ans = S.count('.')
if ans == len(S):
    print(ans)
    exit()
S = S.split('.')
if S:
    S = [(-1)*s.count('S') for s in S if s != '']
heapq.heapify(S)
# Sの列が長いものから処理していく
while k:
    s = heapq.heappop(S) * (-1)
    if s >= 3:
        p = s//3
        if k >= p:
            ans += p * 3
            k -= p
            s -= p * 3
        else:
            ans += k * 3
            k = 0
    elif s >= 2:
        p = s//2
        if k >= p:
            ans += p * 2
            k -= p
            s -= p * 2
        else:
            ans += k * 2
            k = 0
    else:
        p = s
        if k >= p:
            ans += p
            k -= p
            s -= p
        else:
            ans += k
            k = 0
    heapq.heappush(S, s*(-1))
print(ans)
