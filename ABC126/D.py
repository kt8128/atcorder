n = int(input())
tree = [list() for _ in range(n)]
ans = [1] * n
for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))

stack = [0]
judge = [False] * n
while stack:
    node = stack.pop()
    judge[node] = True
    for snode, distance in tree[node]:
        if judge[snode]:
            continue
        if distance % 2 != 0:
            ans[snode] = ans[node] ^ 1
        else:
            ans[snode] = ans[node]
        stack.append(snode)
print(*ans, sep='\n')
