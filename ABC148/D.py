n = int(input())
*A, = map(int, input().split())
num = 1
ans = 0
for i in range(n):
    if A[i] != num:
        ans += 1
    else:
        num += 1
if num == len(A)+1:
    print(0)
elif ans == len(A):
    print(-1)
elif ans:
    print(ans)
else:
    print(-1)
