N = int(input())
H = list(map(int, input().split()))
count = 1
for i in range(N-1):
    if H[i+1] >= max(H[:i+1]):
        count += 1

print(count)
