n = int(input())
B = list(map(int, input().split()))
A = [0] * n
A[0] = B[0]
for i in range(1, n-1):
    if B[i-1] < B[i]:
        A[i] = B[i-1]
    else:
        A[i] = B[i]

A[n-1] = B[n-2]

print(sum(A))
