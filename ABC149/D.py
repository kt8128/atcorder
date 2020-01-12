n, k = map(int, input().split())
r, s, p = map(int, input().split())
T = list(input())
dp = [[0]*3 for _ in range(n)]
for i, t in enumerate(T):
    if t == "r":
        if i < k:
            dp[i][0] += 0
            dp[i][1] += 0
            dp[i][2] += p
        else:
            dp[i][0] = max(dp[i-k][1], dp[i-k][2])
            dp[i][1] = max(dp[i-k][0], dp[i-k][2])
            dp[i][2] = max(dp[i-k][0], dp[i-k][1]) + p
    elif t == "s":
        if i < k:
            dp[i][0] += r
            dp[i][1] += 0
            dp[i][2] += 0
        else:
            dp[i][0] = max(dp[i-k][1], dp[i-k][2]) + r
            dp[i][1] = max(dp[i-k][0], dp[i-k][2])
            dp[i][2] = max(dp[i-k][0], dp[i-k][1])
    else:
        if i < k:
            dp[i][0] += 0
            dp[i][1] += s
            dp[i][2] += 0
        else:
            dp[i][0] = max(dp[i-k][1], dp[i-k][2])
            dp[i][1] = max(dp[i-k][0], dp[i-k][2]) + s
            dp[i][2] = max(dp[i-k][0], dp[i-k][1])
ans = 0
for i in range(k):
    ans += max(dp[n-i-1])
print(ans)
