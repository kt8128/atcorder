h, w = map(int, input().split())
ans = [[0]*w for _ in range(h)]
S = [["#"]*h for _ in range(w)]
for i in range(h):
    s = input().split('#')
    j = 0
    for c in s:
        for d in list(c):
            S[j][i] = d
            ans[i][j] += len(c)
            j += 1
        j += 1
for i in range(w):
    s = "".join(S[i]).split("#")
    j = 0
    for c in s:
        for d in list(c):
            ans[j][i] += len(c)
            j += 1
        j += 1

m = 0
for a in ans:
    if m < max(a):
        m = max(a)
print(m-1)
