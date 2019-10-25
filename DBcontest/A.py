n = int(input())
h = list(map(int, input().split()))
cost = [0 for i in range(n)]
cost[1] = abs(h[1]-h[0])
for i in range(1,n-1):
    cost[i+1] = min(cost[i-1]+abs(h[i-1]-h[i+1]), cost[i]+abs(h[i]-h[i+1]))

print(cost[n-1])
