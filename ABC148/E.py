import math

n = int(input())
if n % 2 == 0:
    ans = 0
    j = 1
    k = 10
    while n // k >= 1:
        # i = math.ceil(n // (5 * k) / 2)
        ans += (n // k)
        k *= 5
    print(ans)
else:
    print(0)
