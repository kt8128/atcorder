n = int(input())
w = list(map(int, input().split()))

m = 10000
for t in range(n-1):
    a = abs(sum(w[:t+1])-sum(w[t+1:]))
    m = min(a, m)
print(m)
