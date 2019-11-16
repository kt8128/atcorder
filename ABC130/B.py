n, x = map(int, input().split())
*L, = map(int, input().split())
d = 0
ans = 1
for l in L:
    d = d + l
    if d <= x:
        ans += 1
print(ans)
