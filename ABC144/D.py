import math

a, b, x = map(int, input().split())
h = (2 * x) / (a ** 2)
A = a
B = 2*b - h

if B < b:
    print(math.degrees(math.atan2(B, A)))
else:
    print(math.degrees(math.atan2(b, (2 * x)/(a * b))))
