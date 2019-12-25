N = int(input())
tree = [list() for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))
stack = [0]
ans = [0] * N
searched = [False] * N
while stack:
    node = stack.pop()
    searched[node] = True
    for v, w in tree[node]:
        if searched[v]:
            continue
        if w % 2 != 0:
            ans[v] = ans[node] ^ 1
        else:
            ans[v] = ans[node]
        stack.append(v)
print(*ans, sep='\n')
