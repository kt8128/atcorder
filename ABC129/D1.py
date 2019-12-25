import re

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))
cnt = [[0]*W for _ in range(H)]
for i in range(H):
    c = 0
    for j in range(W):
        if S[i][j] == '.':
            c += 1
        else:
            c = 0
        cnt[i][j] = c
ans = []
for c in cnt:
    c = [i for i in re.split("(0)", "".join(map(str, c))) if i != '']
    a = []
    for c1 in c:
        c1 = list(c1)
        m = max(c1)
        a += [m]*len(c1)
    ans.append(a)

cnt = [[0]*H for _ in range(W)]
Sr = [list(x) for x in zip(*S)]
for j in range(W):
    c = 0
    for i in range(H):
        if Sr[j][i] == '.':
            c += 1
        else:
            c = 0
        cnt[j][i] = c
ans1 = []
for c in cnt:
    c = [i for i in re.split("(0)", "".join(map(str, c))) if i != '']
    a = []
    for c1 in c:
        c1 = list(c1)
        m = max(c1)
        a += [m]*len(c1)
    ans1.append(a)
ans1 = [list(x) for x in zip(*ans1)]
m = 0
for i in range(H):
    for j in range(W):
        ans[i][j] = int(ans[i][j]) + int(ans1[i][j])
        if m < ans[i][j]:
            m = ans[i][j]
print(m-1)
