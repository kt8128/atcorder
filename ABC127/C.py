from itertools import accumulate

n, m = map(int, input().split())
card = [0] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    card[l-1] += 1
    card[r] -= 1

ans = 0
for i in accumulate(card):
    if i == m:
        ans += 1
print(ans)
