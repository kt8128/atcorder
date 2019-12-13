def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

x, y = map(int, input().split())
mod = 10**9 + 7
if (x + y) % 3 != 0:
    print(0)
    exit()
n = (2*y - x)//3
m = (2*x - y)//3

print(cmb(n+m, n, p))
