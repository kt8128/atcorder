N, K = map(int, input().split())
sum = 0
for i in range(N):
    k = 0
    point = i+1
    while K > point:
        point *= 2
        k += 1
    sum += 1/N * (1/2)**k

print(sum)
