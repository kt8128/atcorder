num = list(input())
num.sort()
idx = num.count('0')
ans = []
ans.append(num[idx])
for i in range(idx):
    ans.append('0')
for n in num[idx+1:]:
    ans.append(n)
print(''.join(ans))
