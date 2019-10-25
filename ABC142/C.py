n = int(input())
a = list(map(int, input().split(' ')))
ans = [0] * n
for i in range(n):
    h = a[i] - 1
    ans[h] = i + 1
print(' '.join(map(str, ans)))
