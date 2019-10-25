from fractions import gcd
from functools import reduce
import itertools
from operator import mul

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under



n = int(input())
a = list(map(int, input().split()))

l = cmb(n, n-1)

print(l)
ans = 0

for itr in l:
    ans = max(ans, reduce(gcd, itr))

print(ans)
