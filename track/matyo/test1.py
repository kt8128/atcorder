from collections import deque

n, m = map(int, input().split())
S = []
check = []
stack = deque()
for y in range(n):
    L = list(input())
    for x, l in enumerate(L):
        if l == "S":
            stack.append((y, x, 0))
            START = (y, x)
        if l == "G":
            GOAL = (y, x)
    S.append(L)
kabe = 10000
while stack:
    y, x, k = stack.pop()
    if k > kabe:
        continue
    if S[y][x] == "#":
        k += 1
    if (y, x) == GOAL:
        if k < kabe:
            kabe = k
        continue
    if START[0] < GOAL[0]:
        if y+1 <= GOAL[0]:
            stack.append((y+1, x, k))
    else:
        if y-1 >= GOAL[0]:
            stack.append((y-1, x, k))
    if START[1] < GOAL[1]:
        if x+1 <= GOAL[1]:
            stack.append((y, x+1, k))
    else:
        if x-1 >= GOAL[1]:
            stack.append((y, x-1, k))
ans = abs(GOAL[0]-START[0])+abs(GOAL[1]-START[1])
for i in range(kabe):
    ans += i
print(ans)
