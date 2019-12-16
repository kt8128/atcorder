n, k = map(int, input().split())
*A, = map(int, input().split())
ans = 0
right = 0
csum = 0
for a in A:
    while (right < n and csum < k):
        csum += A[right]
        right += 1
    if csum >= k:
        ans += n-right+1
    csum -= a
print(ans)
