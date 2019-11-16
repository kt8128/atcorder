N, L = map(int, input().split())
ans = 0
if L >= 0:
    for i in range(1, N):
        ans += i + L
    print(ans)
else:
    if N-1 + L > 0:
        for i in range(N):
            if i + L != 0:
                ans += i + L
        print(ans)
    else:
        for i in range(N-1):
            if i + L != 0:
                ans += i + L
        print(ans)
