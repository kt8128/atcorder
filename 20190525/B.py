r, D, x_2000 = map(int, input().split())
for i in range(10):
    x_next = r * x_2000 - D
    print(x_next)
    x_2000 = x_next
