N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
i = 0
m = 0
flag = 0
for a, f in zip(A, F):
    print(a, f)
for a in A:
    if m+a > K:
        break
    m += a
    flag = a

for _ in range(K):
    if A[i] != 0:
        A[i] -= 1
        if A[i] == 0:
            i += 1
    else:
        i += 1
    if i > len(A)-1:
        break

s = 0
for a, f in zip(A, F):
    print(a, f)
    s += a * f

print(s)
