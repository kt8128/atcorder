import math

N, D = map(int, input().split())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))

a = [i**2 for i in range(300)]
n = 1
t = 0
for i in range(N):
    k = i + n
    for j in range(k, N):
        count = 0
        for l in range(D):
            count += (x[i][l] - x[j][l]) ** 2
        n += 1
        if count in a:
            t += 1
    n = 1

print(t)
