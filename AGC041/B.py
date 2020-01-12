from collections import Counter
import heapq

N, M, V, P = map(int, input().split())
*A, = map(int, input().split())
A = Counter(A)
A = sorted(A.items())
print(A)
ans = 0
t = 0
for a, c in A:
    if c < V-1:
        ans += c
        continue
    else:
        print((A[:t]+A[t+1:])[-V:])
    t += c
print(ans)
