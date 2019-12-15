import heapq
n, m = map(int, input().split())
day = [[] for _ in range(10**5+1)]
for _ in range(n):
    a, b = map(int, input().split())
    day[a].append(b)
benefit = []
heapq.heapify(benefit)
ans = 0
for i in range(1, m+1):
    for j in day[i]:
        heapq.heappush(benefit, -j)
    print(benefit)
    if benefit:
        ans -= heapq.heappop(benefit)  # 最大値を加算
print(ans)
