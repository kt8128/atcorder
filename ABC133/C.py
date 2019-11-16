l, r = map(int, input().split())

if (r-1) * r < 2019:
    print(l * (l+1))
elif r - l > 2019:
    print(0)
else:
    ans = 2019
    for i in range(l, r):
        for k in range(i+1, r+1):
            a = ((i % 2019) * (k % 2019)) % 2019
            if a < ans:
                ans = a
    print(ans)
