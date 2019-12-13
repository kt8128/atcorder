import collections

x, y = map(int, input().split())
d = collections.defaultdict(int)
d[3] = 100000
d[2] = 200000
d[1] = 300000
ans = 0
if x == 1 and y == 1:
    ans += 400000
ans += d[x] + d[y]
print(ans)
