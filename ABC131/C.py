from fractions import gcd

a, b, c, d = map(int, input().split())
lcm = c * d // gcd(c, d)


def nd(n, c, d):
    return n - n // c - n // d + n // lcm


ans = nd(b, c, d) - nd(a-1, c, d)
print(int(ans))
