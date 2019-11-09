def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        a = []
        if n % i == 0:
            a.append(i)
            # divisors.append(i)
            if i != n // i:
                a.append(n//i)
                # divisors.append(n//i)
            else:
                a.append(i)
        divisors.append(a)

    # divisors.sort()
    return divisors

n = int(input())
divisors = make_divisors(n)
min = 10 ** 12
for i in divisors:
    if i:
        if sum(i) < min:
            min = sum(i)

print(min-2)
