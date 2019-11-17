import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)

for _ in range(m):
    max_a = heapq.heappop(a) * (-1)
    heapq.heappush(a, (max_a//2)*(-1))
print(sum(a)*(-1))
