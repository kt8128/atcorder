N = int(input())
ST = []
cnt = 0
for _ in range(N):
    s, t = input().split()
    ST.append([s, t])
    cnt += int(t)
X = input()

for i in range(N):
    s, t = ST[i]
    cnt -= int(t)
    if s == X:
        break
print(cnt)
