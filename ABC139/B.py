a, b = map(int, input().split())
for i in range(30):
    if a * i - (i - 1) >= b:
        print(i)
        break
