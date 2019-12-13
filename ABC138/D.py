n, q = map(int, input().split())
tree = [list() for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
c = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    c[p-1] += x

stack = [0]
j = [False] * n  # すでに探索したか aがbの親とは限らない
while stack:
    node = stack.pop()
    j[node] = True
    for snode in tree[node]:
        if j[snode]:
            continue
        c[snode] += c[node]
        stack.append(snode)

print(*c)
