# # 素因数分解
# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a


t = input().split()
m = t[-1]
AS = []
A = []
for i in t[:-1]:
    a, s = i.split(':')
    AS.append([int(a), s])
    A.append(int(a))
AS = sorted(AS, key=lambda x: x[0])
print(AS)
ans = ''
idx = 0
m = int(m)
for a, s in AS:
    if m % a == 0:
        m = m / a
        ans += s
if ans == '':
    print(m)
else:
    print(ans)
