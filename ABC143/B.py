n = int(input())
d = list(map(int, input().split()))
count = 0
for i in range(n):
    for k in range(i+1, n):
        count += d[i] * d[k]

print(count)
