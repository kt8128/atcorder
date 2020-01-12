n, a, b = map(int, input().split())
if (b-a) % 2 == 0:
    print((b-a)//2)
else:
    if n-a <= b-1:
        if n-b+1 < n-a:
            print((n-(a+(n-b+1)))//2+(n-b+1))
        else:
            print(n-a)
    else:
        if a-1+1 < b-1:
            print((b-(a-1+1)-1)//2+(a-1+1))
        else:
            print(b-1)
