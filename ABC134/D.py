def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n = int(input())
a = list(map(int, input().split()))
box = [0 for _ in range(n)]
sum_box = [0 for _ in range(n)]
for i in range(n)[::-1]:
    if a[i] == 1 and sum_box[i] % 2 == 0:
        for k in make_divisors(i+1):
            sum_box[k-1] += 1
        box[i] = 1
    elif a[i] == 1 and sum_box[i] % 2 != 0:
        box[i] = 0
    elif a[i] != 1 and sum_box[i] % 2 != 0:
        for k in make_divisors(i+1):
            sum_box[k-1] += 1
        box[i] = 1
    elif a[i] != 1 and sum_box[i] % 2 == 0:
        box[i] = 0
ans = []
for i, b in enumerate(box):
    if b == 1:
        ans.append(str(i+1))
if not ans:
    print(0)
else:
    s = ' '.join(ans)
    print(len(ans))
    print(s)
