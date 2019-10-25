import math
import itertools
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n, k = map(int, input().split())
for i in range(k):
    if n-k+1 < i:
        print(0)
    else:
        print(((cmb(n-k+1, i+1) % (10 ** 9 + 7)) * (cmb(k-1, i) % (10 ** 9 + 7))) % (10 ** 9 + 7))
