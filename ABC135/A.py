a, b = map(int, input().split())
if abs(a-b) % 2 != 0:
    print('IMPOSSIBLE')
else:
    print(abs(a-b) // 2 + min(a, b))
