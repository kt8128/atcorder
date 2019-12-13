n = int(input())
A = list(map(int, input().split()))

s = sum(A)
idx = 0
s1 = 0
half = s//2
for i, a in enumerate(A):
    s1 += a
    if half < s1:
        idx = i
        break

s2 = sum(A[i+1:])
ans1 = abs(s1-s2)
s3 = sum(A[i:])
ans2 = abs(s1-s3-A[i])
print(min([ans1, ans2]))
