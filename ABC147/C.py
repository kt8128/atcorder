from itertools import product

N = int(input())
B = list(product([1, 0], repeat=N))
L = []
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        L.append([x, y, i+1])
ans = 0
for b in B:
    for l in L:
        if b[l[2]-1] == 1 and l[1] != b[l[0]-1]:
            break
    else:
        if ans < b.count(1):
            ans = b.count(1)
print(ans)
