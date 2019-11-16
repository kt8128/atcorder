n = int(input())
*a, = map(int, input().split())
ans = 0
for i in a:
    ans += 1/i
print(1/ans)
