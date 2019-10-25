n = int(input())
v = list(map(int, input().split()))

v.sort()

while len(v) != 1:
    a = v.pop(0)
    b = v.pop(0)
    v.insert(0, (a+b)/2)

print(v[0])
