def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a, b):
    return gcd(a, b) == 1


def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


a, b = map(int, input().split())
d_a = set(make_divisors(a))
d_b = set(make_divisors(b))
matched_list1 = list(d_a & d_b)

count = 0

for i in matched_list1:
    if is_prime(i):
        count += 1

print(count+1)
