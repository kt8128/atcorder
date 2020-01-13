n, k, m = map(int, input().split())
*A, = map(int, input().split())
s = sum(A)
if n*m-s > k:
    print(-1)
else:
    print(max(n*m-s, 0))
