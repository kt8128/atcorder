from collections import deque

n, m = map(int, input().split())
S = []
check = []
stack = deque()
for y in range(n):
    L = list(input())
    for x, l in enumerate(L):
        if l == "S":
            stack.append((y, x, 0, 0))
            START = (y, x)
        if l == "G":
            GOAL = (y, x)
    S.append(L)
ans = 10000
while stack:
    y, x, score, hirou = stack.pop()
    if S[y][x] == "#":
        score += hirou + 1
        hirou += 1
    elif S[y][x] == '.':
        score += 1
    if (y, x) == GOAL:
        if score < ans:
            ans = score+1
        continue
    if START[0] < GOAL[0]:
        if y+1 <= GOAL[0]:
            stack.append((y+1, x, score, hirou))
    else:
        if y-1 >= GOAL[0]:
            stack.append((y-1, x, score, hirou))
    if START[1] < GOAL[1]:
        if x+1 <= GOAL[1]:
            stack.append((y, x+1, score, hirou))
    else:
        if x-1 >= GOAL[1]:
            stack.append((y, x-1, score, hirou))
print(ans)
