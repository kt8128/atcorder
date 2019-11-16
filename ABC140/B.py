n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
*c, = map(int, input().split())
ans = 0
ans += b[a[0]-1]
for i in range(1, n):
    ans += b[a[i]-1]
    if a[i] == a[i-1] + 1:
        ans += c[a[i-1]-1]
print(ans)
