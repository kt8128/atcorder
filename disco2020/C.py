h, w, k = map(int, input().split())
m = []
for i in range(h):
    m.append(list(input()))

ans = []
for i in range(h):
    ans.append([0 for _ in range(w)])

if m[0][0] == '#':
    c = 0
else:
    c = 1
emp = []
for i in range(h):
    s1 = 0
    s = m[i].count('#')
    # 行に一つもいちごがない
    if s == 0:
        emp.append(i)
        continue
    for j in range(w):
        flag = 0
        if m[i][0] == '#':
            if m[i][j] == '#':
                if s1 < s and c < k:
                    s1 += 1
                    c += 1
            ans[i][j] = c
        else:
            ans[i][j] = c
            if m[i][j] == '#':
                flag = 1
                if s1 < s-1 and c < k:
                    s1 += 1
                    c += 1
    if i != h-1 and m[i+1][0] != '#':
        c += 1

if 0 in emp:
    for j in range(w):
        for i1 in range(1, h):
            if ans[i1][0] != 0:
                idx = ans[i1]
                break
        ans[0][j] = idx[j]
    emp.remove(0)
if h-1 in emp:
    for j in range(w):
        for i1 in list(range(h-1))[::-1]:
            if ans[i1][0] != 0:
                idx = ans[i1]
                break
        ans[h-1][j] = idx[j]
    emp.remove(h-1)
for e in emp:
    for j in range(w):
        idx = []
        for i1 in range(e+1, h):
            if ans[i1][0] != 0:
                idx = ans[i1]
                break
        ans[e][j] = idx[j]

for i in ans:
    print(' '.join(map(str, i)))
