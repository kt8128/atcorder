n = int(input())
h = list(map(int, input().split()))
count = 0
c = []

for i in range(1, n):
    if h[i-1] >= h[i]:
        count += 1
    else:
        c.append(count)
        count = 0
c.append(count)

print(max(c))
