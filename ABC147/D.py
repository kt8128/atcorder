n = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
array = [0] * 60
for a in A:
    for j in range(len(bin(a))-2):
        array[j] += (a >> j) & 1
ans = 0
for i in range(60):
    ans += array[i] * (n-array[i]) * 2**i
print(ans % mod)
