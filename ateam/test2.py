n = int(input())
ans = []
for i in range(1, n+1):
    for k in range(1, n+1):
        ans.append(i*i*k)
print(len(set(ans)))
