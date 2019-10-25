import numpy as np

N, W = map(int, input().split())
# dp[i] : 価値iを作れる時の重さの最小値
dp = np.full(N*100+1, W+1, 'i8')
dp[0] = 0
for i in range(N):
    w, v = map(int, input().split())
    dp[v:] = np.minimum(dp[v:], dp[:-v]+w)
print(np.max(np.where(dp<=W)))


# l = [0,1,2,3,4,5,6]
# print(l[:-1])
