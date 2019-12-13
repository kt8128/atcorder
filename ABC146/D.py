from collections import deque

n = int(input())
t = [list() for _ in range(n)]
color = [0] * (n-1)

for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    t[a].append((b, i))
q = deque([(0, 0)])
while q:
    v, pc = q.popleft()
    nc = 0
    for nv, edge in t[v]:
        nc += 1
        if nc == pc:
            nc += 1
        color[edge] = nc
        q.append((nv, nc))

print(max(color))
print(*color, sep="\n")
