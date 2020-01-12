a, b, k = map(int, input().split())
if k >= a:
    b -= k-a
    a = 0
else:
    a -= k
print(max(a, 0), max(b, 0))
