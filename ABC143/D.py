import bisect

n = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        k = bisect.bisect_left(L[j+1:], L[i]+L[j])
        count += k

print(count)
