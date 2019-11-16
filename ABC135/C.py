n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(n):
    if A[i] < B[i]:
        count += A[i]
        B[i] -= A[i]
        A[i] = 0
    else:
        count += B[i]
        A[i] -= B[i]
        B[i] = 0
    if B[i]:
        if A[i+1] < B[i]:
            count += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            count += B[i]
            A[i+1] -= B[i]
            B[i] = 0

print(count)
