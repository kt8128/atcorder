w, h, x, y = map(int, input().split())

ans = w * h / 2
if 2 * x == w and 2 * y == h:
    print(ans, 1)
else:
    print(ans, 0)
