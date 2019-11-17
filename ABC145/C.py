import math

n = int(input())
cnt = 0
x = []
y = []
for _ in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        cnt += math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
print(cnt/n)
