s = input()
tmp = [0]
for i in range(len(s)-1):
    if s[i] != s[i+1]:  # RとLが切り替わる時のインデックスを保存
        tmp.append(i+1)
tmp.append(len(s))
print(tmp)
ans = [0 for i in range(len(s))]
for i in range(len(tmp)-1):
    if i % 2 == 1:
        ans[tmp[i]] = (tmp[i]-tmp[i-1])//2 + (tmp[i+1]-tmp[i]+1)//2
        ans[tmp[i]-1] = (tmp[i+1]-tmp[i])//2 + (tmp[i]-tmp[i-1]+1)//2
print(*ans)
# RRLLLLRLRRLL
# tmp=[0, 2, 6, 7, 8, 10, 12]
