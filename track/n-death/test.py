def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


l, r = map(int, input().split())
m = int(input())
*N, = map(int, input().split())
N.sort()
cnt = 0
check = []
for i, n in enumerate(N):
    cnt += r//n - l//n
    if r % n == 0 and l % n == 0:
        cnt += 1
    for n1 in N[:i]:
        n1 = lcm(n, n1)
        cnt -= r//n1 - l//n1
print((r-l+1)-cnt)
