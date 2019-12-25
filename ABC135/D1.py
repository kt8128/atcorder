S = list(input())
dp = [[0]*13 for j in range(len(S)+1)]
dp[0][0] = 1
mod = 10**9 + 7
k = 1
for i, s in enumerate(S[::-1]):
    if s == '?':
        for c in range(10):
            for j in range(13):
                dp[i+1][(k*c+j) % 13] += dp[i][j] % mod
    else:
        c = int(s)
        for j in range(13):
            dp[i+1][(k*c+j) % 13] += dp[i][j] % mod
    k = k * 10 % 13
print(dp[-1][5] % mod)
